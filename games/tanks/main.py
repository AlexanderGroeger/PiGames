import pygame
from lib.game import Game
from lib.input.controller import GameCubeController
import lib.globals as G

import os

class Driver(Game):

    def __init__(self):
        G.gameWidth, G.gameHeight = (640, 360)
        super().__init__()
        self.bgcolor = (192,)*3

        G.CP = G.mm.getModule("color_palettes")

        tankModule = G.mm.getModule("tank")
        tankModule.init()
        Tank = tankModule.PlayerTank

        pygame.joystick.init()
        self.joystick_count = pygame.joystick.get_count()
        self.controllers = []
        for i in range(self.joystick_count):
            controller = GameCubeController(pygame.joystick.Joystick(i))
            controller.joystick.init()
            self.controllers.append(controller)
        self.tanks = []
        self.tanks.append(Tank(self.controllers[-1],colors = G.CP.GREEN, build = G.BASIC,xy=(35,75)))
        G.objects+=self.tanks

    def step(self):
        super().step()
        for controller in self.controllers:
            controller.step()

def start():
    game = Driver()
    game.run()
