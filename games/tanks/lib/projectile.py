from lib.abstract import Object
import lib.globals as G
import numpy as np

class Projectile(Object):
    def __init__(self,owner,**kwargs):
        self.owner = owner
        super().__init__(**kwargs)

class Bullet(Projectile):
    def __init__(self,bulletType=0, angle = 0,**kwargs):
        self.bulletType = bulletType
        super().__init__(**kwargs)
        self.angle = angle
        self.vspeed = -1.5*np.sin(angle*np.pi/180)
        self.hspeed = 1.5*np.cos(angle*np.pi/180)
        self.initSprites()

    def initSprites(self):
        if self.bulletType == G.BASIC:
            self.gfxBullet = G.SMALL_BULLET_GRAPHICS

    def step(self):
        # if self.hspeed == 0:
        #     self.angle = int(np.sign(-self.vspeed)*90)%360
        # elif self.vspeed == 0:
        #     self.angle = int(self.hspeed<0)*180
        # else:
        #     self.angle = int(np.arctan2(-self.vspeed,self.hspeed)/np.pi*180)%360
        # self.angle = np.arctan2(self.vspeed,self.hspeed)
        print(self.angle)
        super().step()

    def draw(self,surf):
        surf.blit(
            self.gfxBullet.tiles[(int((self.angle+360/16/2)//(360/16))%16)],
            (self.x-2,self.y-2),
        )
