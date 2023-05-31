from lib.abstract import Instance
from lib.text import Text
from lib.input.gamecube import *
import lib.globals as G
import pygame

class ProgressBar(Instance):
    def __init__(self,**kwargs):

        self.width = 128
        self.height = 16
        self.outlineColor = pygame.Color(255,255,255)
        self.barColor = pygame.Color(192,192,192)
        self.progress = 0
        self.outlineThickness = 2
        self.halign = 'center'
        self.acceleration = 0

        for key in list(kwargs.keys()):
            if getattr(self,key,None) is not None:
                setattr(self,key,kwargs.pop(key))

        self.inputListeners = dict()
        self.inputListeners[pygame.JOYBUTTONDOWN] = self.controllerButtonDown
        # self.inputListeners[pygame.JOYBUTTONUP] = self.controllerButtonUp
        self.controllersPressed = {}
        self.synchronizedPresses = 0
        self.locked = False
        super().__init__(**kwargs)

    def setProgress(self,p):
        self.progress = max(0,min(1,p))

    def drawOutline(self,surf):

        if self.halign == 'center':
            dx, dy = self.x - self.width//2, self.y - self.height//2
        elif self.halign == 'left':
            dx, dy = self.x, self.y
        elif self.halign == 'right':
            dx, dy = self.x - self.width, self.y - self.height

        outlineRect = pygame.Rect(dx,dy,self.width,self.height)
        pygame.draw.rect(surf,self.outlineColor,outlineRect,self.outlineThickness)

    def drawProgress(self,surf):

        if self.halign == 'center':
            dx, dy = self.x - (self.width - self.outlineThickness * 2)//2, self.y + self.outlineThickness - self.height//2
        elif self.halign == 'left':
            dx, dy = self.x + self.outlineThickness, self.y + self.outlineThickness
        elif self.halign == 'right':
            dx, dy = self.x - (self.width - self.outlineThickness * 2), self.y + self.outlineThickness - self.height

        dw = int(self.progress * (self.width - self.outlineThickness * 2))
        dh = self.height - self.outlineThickness*2

        barRect = pygame.Rect(dx,dy,dw,dh)

        surf.fill(self.barColor,barRect)

    def controllerButtonDown(self,event):
        controller = G.controllers.get(str(event.instance_id),{})
        if event.button == getattr(controller,"PRIMARY_BUTTON",None):
            self.acceleration += 2
            if event.instance_id not in self.controllersPressed:
                self.controllersPressed[str(event.instance_id)] = controller

    # def controllerButtonUp(self,event):
    #     controller = G.controllers.get(str(event.instance_id),{})
    #     if event.button == getattr(controller,"PRIMARY_BUTTON",None) and str(event.instance_id) in self.controllersPressed:
    #         del self.controllersPressed[str(event.instance_id)]

    def input(self):
        for event in G.events:
            for eventType, callback in self.inputListeners.items():
                if event.type == eventType:
                    callback(event)


    def draw(self,surf):
        self.drawOutline(surf)
        self.drawProgress(surf)

    def step(self):

        instance_ids_to_remove = []
        for instance_id, controller in self.controllersPressed.items():
            if controller.framesButtonHeld[controller.PRIMARY_BUTTON] > 2:
                instance_ids_to_remove.append(instance_id)

        for instance_id in instance_ids_to_remove:
            del self.controllersPressed[instance_id]

        self.synchronizedPresses = len(self.controllersPressed)

        if self.synchronizedPresses > 1:
            self.acceleration += (self.synchronizedPresses+1)*self.synchronizedPresses//2

        self.acceleration = max(0,self.acceleration-1)
        if not self.locked:
            self.setProgress(0.99*self.progress+0.003*self.acceleration)
        if self.progress == 1:
            self.locked = True
