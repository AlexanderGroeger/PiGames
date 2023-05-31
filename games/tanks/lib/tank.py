from lib.abstract import Object
from lib.input.gamecube import *
import lib.globals as G
import pygame
import numpy as np


def init():
    G.Bullet = G.mm.getModule("projectile").Bullet
    G.BASIC = 0
    G.BASIC_TANK_BODY_GRAPHICS = G.am.getTileset("tank/basic/body",size=32)
    G.SMALL_BULLET_GRAPHICS = G.am.getTileset("tank/basic/small_bullet",size=4)
    G.BASIC_TANK_CAP_GRAPHIC = G.am.getGraphic("tank/basic/cap")
    G.BASIC_TANK_BARREL_GRAPHICS = G.am.getTileset("tank/basic/barrel",size=32)

class Tank(Object):
    def __init__(self,speed = 1, colors = None, build = 0,**kwargs):
        super().__init__(**kwargs)
        self.tankSpeed = speed
        self.tankAngle = 0
        self.aimAngle = 0
        self.previousAngles = [0]*2
        self.colors = colors
        self.build = build
        self.initSprites()

    def initSprites(self):
        if self.build == G.BASIC:
            self.gfxBarrel = self.recolor(G.BASIC_TANK_BARREL_GRAPHICS)
            self.gfxBody = self.recolor(G.BASIC_TANK_BODY_GRAPHICS)
            self.gfxBullet = self.recolor(G.SMALL_BULLET_GRAPHICS)
            self.gfxCap = self.recolor(G.BASIC_TANK_CAP_GRAPHIC)

    def recolor(self,tileset):
        if self.colors:
            if hasattr(tileset,"tiles"):
                for i, tile in enumerate(tileset.tiles):
                    pa = pygame.PixelArray(tile)
                    for (col, repcol) in zip(G.CP.DEFAULT,self.colors):
                        pa.replace(col,repcol)
                    tileset.tiles[i] = pa.surface
            else:
                pa = pygame.PixelArray(tileset)
                for (col, repcol) in zip(G.CP.DEFAULT,self.colors):
                    pa.replace(col,repcol)
                tileset = pa.surface
        return tileset

    def step(self):
        super().step()
        # Collision

    def draw(self,surf):
        # pygame.draw.circle(surf,(32,)*3,(self.x,self.y),7)
        surf.blit(
            pygame.transform.rotate(
                self.gfxBody.tiles[int((self.tankAngle+45/4)//(45/2))%4],
                ((self.tankAngle+45/4)//90*90),
            ),
            (self.x-16,self.y-16),
        )
        surf.blit(
            self.gfxBarrel.tiles[(int((self.aimAngle+360/24/2)//(360/24))%24)],
            (self.x-16,self.y-16),
        )
        surf.blit(
            self.gfxCap,
            (self.x-16,self.y-16),
        )

PlayerCrosshairs = G.mm.getModule("crosshairs").PlayerCrosshairs

class PlayerTank(Tank):
    def __init__(self,controller = None, **kwargs):
        super().__init__(**kwargs)
        self.controller = controller
        kwargs.pop("xy",None)
        self.crosshairs = PlayerCrosshairs(
            anchor = self,
            controller = self.controller,
            speed = 3,
            depth = -100,
            xy = (self.x + 32, self.y),
            **kwargs
        )
        self.aimAngle = 0
        G.objects.append(self.crosshairs)

    def getMovementStickPosition(self):
        return self.controller.joystick.get_axis(HSTICK1), self.controller.joystick.get_axis(VSTICK1)

    def getAimStickPosition(self):
        return self.controller.joystick.get_axis(HSTICK2), self.controller.joystick.get_axis(VSTICK2)

    def step(self):
        jh, jv = self.getMovementStickPosition()
        jh = np.sign(jh)*(np.floor(np.abs(jh)*20)/20)
        jv = np.sign(jv)*(np.floor(np.abs(jv)*20)/20)
        if jh or jv:
            if jh == 0:
                theta = int(np.sign(-jv)*90)%360
            elif jv == 0:
                theta = int(jh<0)*180
            else:
                theta = int(np.arctan2(-jv,jh)/np.pi*180)%360
            # self.previousAngles.pop(0)
            # self.previousAngles.append(theta)
            #
            # if np.all(theta == np.array(self.previousAngles)):
            #     print(self.previousAngles)
            #     self.tankAngle = theta
            self.tankAngle = theta

        self.hspeed = self.tankSpeed*jh
        self.vspeed = self.tankSpeed*jv

        cdx = self.crosshairs.x - self.x
        cdy = self.crosshairs.y - self.y
        if cdx or cdy:
            if cdx == 0:
                theta = int(np.sign(-cdy)*90)%360
            elif cdy == 0:
                theta = int(cdx<0)*180
            else:
                theta = int(np.arctan2(-cdy,cdx)/np.pi*180)%360
            self.aimAngle = theta

        if self.controller.joystick.get_button(LEFT_SHOULDER_BUTTON) and self.controller.framesButtonHeld[LEFT_SHOULDER_BUTTON] == 0:
            dx, dy = 15*np.cos(self.aimAngle*np.pi/180), -15*np.sin(self.aimAngle*np.pi/180)
            bullet = G.Bullet(owner=self,bulletType=self.build,angle=self.aimAngle,xy=(self.x+dx,self.y+dy))
            G.objects.append(bullet)
            print(self.aimAngle)
        super().step()
