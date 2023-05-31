import os
from importlib import import_module
import lib.globals as G

class ModuleManager:
    def getModule(self, fname):
        return import_module(f"{G.gameDir.replace('/','.')}.lib.{fname}")
