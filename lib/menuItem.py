from lib.abstract import Instance
from lib.text import Text
import lib.globals as G

import numpy as np
from pygame import mixer

class MenuItem(Instance):
    def __init__(self, callback=None, inst=None, adj={}, selectedAnimation=None, **kwargs):
        self.callback = callback
        self.selected = False
        self.inst = inst
        self.adjItems = adj
        self.selectedAnimation = selectedAnimation
        self.selectedAnimationTimer = 0
        self.selectedAnimationStartTick = 0
        super().__init__(**kwargs)

    def getAdjacencyGraph(self,adj):
        return self.adjItems

    def updateAdjacencyGraph(self,adj):
        self.adjItems.update(adj)

    def changeSelection(self,direction):
        self.clearSelection()
        self.adjItems[direction].setSelected()
        sound = G.am.getSound("enter")
        sound.play()

    def setSelected(self):
        self.selected = True
        self.selectedAnimationStartTick = G.t

    def clearSelection(self):
        self.selected = False

    def select(self):
        if callable(self.callback):
            self.callback()

    def step(self):
        if self.inst:
            self.animate()

    def draw(self,surf):
        if self.inst:
            self.inst.draw(surf)

    def animate(self):
        if self.selected:
            if self.selectedAnimation is not None:
                dx, dy = self.selectedAnimation(self.selectedAnimationStartTick)
                self.inst.x = self.x + dx
                self.inst.y = self.y + dy
        else:
            self.inst.x = self.x
            self.inst.y = self.y

class TextMenuItem(MenuItem):
    def __init__(self, text = "", alphaBright = 255, alphaDim = 127, **kwargs):
        super().__init__(inst = Text(text,**kwargs), **kwargs)
        self.alphaBright = alphaBright
        self.alphaDim = alphaDim
        self.clearSelection()

    def setSelected(self):
        super().setSelected()
        self.inst.setAlpha(self.alphaBright)

    def clearSelection(self):
        super().clearSelection()
        self.inst.setAlpha(self.alphaDim)
