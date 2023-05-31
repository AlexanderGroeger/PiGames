import pygame
import lib.globals as G

from lib.text import Text
from lib.menuItem import MenuItem, TextMenuItem
import traceback

class Menu:

    def __init__(self,items,connections = None):

        self.confirmButton = pygame.K_RETURN
        self.inputListeners = dict()
        self.inputListeners[pygame.KEYDOWN] = self.keyDown
        self.inputListeners[pygame.JOYBUTTONDOWN] = self.controllerButtonDown

        if connections:
            for item,adj in zip(items,connections):
                item.updateAdjacencyGraph(connections)

        self.items = items
        self.selectOption(0)

    def addItem(self,item):
        self.items.append(item)

    def selectOption(self,index):
        self.selectedIndex = max(0,min(index,len(self.items)-1))
        self.items[self.selectedIndex].setSelected()

    def keyDown(self,event):
        if event.key == self.confirmButton:
            self.items[self.selectedIndex].select()

    def controllerButtonDown(self,event):
        controller = G.controllers.get(str(event.instance_id),{})
        if event.button == getattr(controller,"PRIMARY_BUTTON",None):
            self.items[self.selectedIndex].select()

    def input(self):
        for event in G.events:
            for eventType, callback in self.inputListeners.items():
                if event.type == eventType:
                    callback(event)

    def step(self):
        for item in self.items:
            item.step()

    def draw(self,surf):
        for item in self.items:
            item.draw(surf)

class LinearMenu(Menu):

    def __init__(self,items,vertical = True):

        self.isVertical = vertical
        if vertical:
            self.dirPrev = pygame.K_UP
            self.dirNext = pygame.K_DOWN
        else:
            self.dirPrev = pygame.K_LEFT
            self.dirNext = pygame.K_RIGHT
        self.dirToInt = {self.dirPrev: -1, self.dirNext: 1}

        for i in range(len(items)):
            adj = {}
            if (i > 0):
                adj.update({"-1": items[i-1]})
            if (i < len(items) - 1):
                adj.update({"1": items[i+1]})

            items[i].updateAdjacencyGraph(adj)

        super().__init__(items)
        self.inputListeners[pygame.JOYAXISMOTION] = self.controllerAxisChanged

    def addItem(self,item):
        item.updateAdjacencyGraph({"-1": self.items[-1]})
        self.items[-1].updateAdjacencyGraph({"1": item})
        self.items.append(item)

    def changeSelection(self,direction):
        newIndex = self.selectedIndex + direction
        if (newIndex) in range(len(self.items)):
            self.items[self.selectedIndex].clearSelection()
            self.selectOption(newIndex)
            sound = G.am.getSound("select")
            sound.set_volume(0.25)
            sound.play()

    def controllerAxisChanged(self,event):
        controller = G.controllers.get(str(event.instance_id),{})
        dir = int(event.value > .5) - int(event.value < -.5)
        if dir != 0:
            if event.axis == getattr(controller,f"PRIMARY_{'V' if self.isVertical else 'H'}_AXIS",None):
                self.changeSelection(dir)

    def keyDown(self,event):
        if event.type == pygame.KEYDOWN:
            super().keyDown(event)
            if event.key in (self.dirPrev, self.dirNext):
                self.changeSelection(self.dirToInt[event.key])


class LinearTextMenu(LinearMenu):
    def __init__(self,textOptions,hspace=0,vspace=0,**kwargs):
        items = []
        for i, (optionText, callback) in enumerate(textOptions.items()):
            tmi = TextMenuItem(optionText,callback=callback,**kwargs)
            tmi.x += hspace*i
            tmi.y += vspace*i
            tmi.inst.x = tmi.x
            tmi.inst.y = tmi.y
            items.append(tmi)
        super().__init__(items,vertical = kwargs.get("vertical",True))
