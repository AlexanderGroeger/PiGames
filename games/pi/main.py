from pygame.display import set_caption
from lib.game import Game
from lib.sceneManager import SceneManager

import lib.globals as G

class Driver(Game):

    def __init__(self):

        G.gameWidth, G.gameHeight = (256, 144)
        G.windowFullScreen = False
        G.sm = SceneManager()

        super().__init__()
        set_caption("Pi Games")
        G.sm.goToScene(0)

def start():
    G.game = Driver()
    G.game.run()
