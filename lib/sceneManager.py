import os
import glob
from importlib import import_module

import lib.globals as G

class SceneManager:
    def __init__(self):
        self.sceneNum = -1
        self.scene = None

    def getScene(self, n):
        return import_module(f"{G.gameDir.replace('/','.')}.scenes.{n}").Main()

    def goToScene(self,n):
        G.backgrounds = []
        G.objects = []
        self.sceneNum = n
        self.scene = G.sm.getScene(n)
        self.scene.start()

    def nextScene(self):
        self.sceneNum += 1
        self.goToScene(self.sceneNum)
