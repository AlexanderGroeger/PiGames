from pygame.display import set_caption
from lib.game import Game
from lib.sceneManager import SceneManager

import lib.globals as G

class Driver(Game):

    def __init__(self):

        G.gameWidth, G.gameHeight = (512, 288)
        G.sm = SceneManager()

        super().__init__()
        set_caption("TextStory")
        G.sm.goToScene(0)

def start():
    G.game = Driver()
    G.game.run()
