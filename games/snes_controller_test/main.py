import pygame
from lib.game import Game
import lib.globals as G

import os

Controller = G.mm.getModule("controller").Controller

class Driver(Game):

    def __init__(self):
        super().__init__()
        self.bgcolor = (24, 24, 24)

        G.SNES_GRAPHICS = {}
        for filename in os.listdir(f"{G.gameDir}/graphics/buttons"):
            G.SNES_GRAPHICS[filename.split('.')[0]] = G.am.getGraphic(f"buttons/{filename.split('.')[0]}",alpha=True)

        n = 16
        G.SNES_GRAPHIC_POSITION = {
            "left_shoulder": (n*0.5,0),
            "right_shoulder": (n*7.5,0),
            "dpad_up": (n*0.75,n*1),
            "dpad_down": (n*0.75,n*2.5),
            "dpad_left": (n*0,n*1.75),
            "dpad_right": (n*1.5,n*1.75),
            "start": (n*4.25,n*2.75),
            "select": (n*3,n*2.75),
            "a": (n*8,n*1.75),
            "b": (n*7,n*2.5),
            "y": (n*6,n*1.75),
            "x": (n*7,n*1),
            "device_num": (n*3.625,n*1.25),
        }
        pygame.joystick.init()
        self.joystick_count = pygame.joystick.get_count()
        self.controllers = []
        for i in range(self.joystick_count):
            c = Controller(
                pygame.joystick.Joystick(self.joystick_count-i-1),
                xy = (
                    2*n+(i % 4)*n*10,
                    3*n//2+(i // 4)*n*7,
                ),
            )
            self.controllers.append(c)
            G.objects.append(c)

def start():
    game = Driver()
    game.run()
