import pygame
from lib.game import Game
import lib.globals as G

import os

Controller = G.mm.getModule("controller").Controller

class Driver(Game):

    def __init__(self):
        super().__init__()
        self.bgcolor = (70, 63, 111)

        G.GAMECUBE_GRAPHICS = {}
        for filename in os.listdir(f"{G.gameDir}/graphics/buttons"):
            G.GAMECUBE_GRAPHICS[filename.split('.')[0]] = G.am.getGraphic(f"buttons/{filename.split('.')[0]}")

        G.GAMECUBE_GRAPHIC_POSITION = {
            "left_shoulder": (0,0),
            "right_shoulder": (64*6,0),
            "joystick": (64*0,64*1.75),
            "start": (64*3,64*1.75),
            "a": (64*6,64*1.75),
            "b": (64*(6-1),64*(1.75+.5)),
            "y": (64*(6-.25),64*(1.75-1)),
            "x": (64*(6+1),64*(1.75-.25)),
            "z": (64*(6-1.25),64*(1.75-1.5)),
            "dpad": (64*1.5,64*3.75),
            "cstick": (64*4.5,64*3.75),
        }
        pygame.joystick.init()
        self.joystick_count = pygame.joystick.get_count()
        self.controllers = []
        for i in range(self.joystick_count):
            c = Controller(
                pygame.joystick.Joystick(self.joystick_count-i-1),
                xy = (
                    128+(i % 2)*64*10,
                    96+(i // 2)*64*7,
                )
            )
            self.controllers.append(c)
            G.objects.append(c)

def start():
    game = Driver()
    game.run()
