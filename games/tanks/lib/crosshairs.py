from lib.input.gamecube import *
from lib.abstract import Object
import pygame
import numpy as np

class Crosshairs(Object):
    def __init__(self,anchor,speed = 5,**kwargs):
        self.anchor = anchor
        self.speed = speed
        super().__init__(**kwargs)

    def draw(self,surf):
        pygame.draw.line(surf,
            self.anchor.colors[1],
            (self.x-4,self.y-4),
            (self.x+4,self.y+4),
            width = 2,
        )
        pygame.draw.line(surf,
            self.anchor.colors[1],
            (self.x+4,self.y-4),
            (self.x-4,self.y+4),
            width = 2,
        )
        dx, dy = self.x - self.anchor.x, self.y - self.anchor.y
        dist = np.linalg.norm([dx,dy])
        n = 5 #min(int(dist // 50),5)
        for (lx,ly) in zip(np.linspace(self.x,self.anchor.x,n+2)[1:-1].astype(np.uint16),np.linspace(self.y,self.anchor.y,n+2)[1:-1].astype(np.uint16)):
            pygame.draw.rect(surf,self.anchor.colors[1],
                pygame.Rect(lx - 1, ly - 1, 2, 2)
            )

class PlayerCrosshairs(Crosshairs):
    def __init__(self,controller,**kwargs):
        self.controller = controller
        super().__init__(**kwargs)

    def step(self):
        jh, jv = self.anchor.getAimStickPosition()
        jh = np.sign(jh)*(np.floor(np.abs(jh)*20)/20)
        jv = np.sign(jv)*(np.floor(np.abs(jv)*20)/20)
        self.hspeed = self.speed*jh
        self.vspeed = self.speed*jv
        super().step()
