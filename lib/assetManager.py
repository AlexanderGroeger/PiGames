import os
import glob

from pygame.font import SysFont, Font
from pygame.image import load
from pygame import mixer

from lib.background import Background
from lib.tiles import Tileset
import lib.globals as G

class AssetManager:
    
    def getGraphic(self, fname, alpha=False):
        path = glob.glob(f'{G.gameDir}/graphics/{fname}.*')[0]
        if alpha:
            return load(path).convert_alpha()
        else:
            return load(path).convert()

    def getTileset(self, fname, **kwargs):
        path = glob.glob(f'{G.gameDir}/graphics/{fname}.*')[0]
        tileset = Tileset(path,**kwargs)
        return tileset

    def getFont(self, fname, fsize):
        font = None
        try:
            font = SysFont(fname, fsize)
        except:
            font = Font(glob.glob(f'{G.gameDir}/font/{fname}.*')[0], fsize)
        return font

    def loadMusic(self, fname):
        return mixer.music.load(glob.glob(f'{G.gameDir}/audio/music/{fname}.*')[0])

    def getSound(self, fname):
        return mixer.Sound(glob.glob(f'{G.gameDir}/audio/sound/{fname}.*')[0])
