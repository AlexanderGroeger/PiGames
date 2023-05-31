from pygame.image import load
from lib.object import Object

class ScollingBackground(Background):

    def __init__(self, wrap = False, *args, **kwargs):
        Object.__init__(self, *args, **kwargs)
        self.wrap = wrap

    def step(self):
        self.x += self.hspeed
        self.y += self.vspeed
        if self.wrap:
            self.x %= self.w
            self.y %= self.h
        else:
            self.x = max(self.w,min(self.x,-self.w))
            self.y = max(self.h,min(self.y,-self.h))

    def draw(self,surf):
        surf.blit(self.surf,(self.x,self.y),(0,0,self.w,self.h))
        if self.wrap:
            if self.x > 0 and self.y == 0:
                surf.blit(self.surf,(0,0),(self.w-self.x,0,self.x,self.h))
