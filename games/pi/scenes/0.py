import pygame
from pygame import mixer

from lib.scene import Scene
from lib.background import Background, ScrollingBackground
from lib.text import Text
from lib.menu import LinearTextMenu

import lib.globals as G

ProgressBar = G.mm.getModule("progress_bar").ProgressBar

class Main(Scene):

    def __init__(self):
        super().__init__()

    def start(self):

        G.am.loadMusic("blackoutcity")
        mixer.music.play(-1)

        background = Background(
            img = G.am.getGraphic(f"background/night")
        )
        G.backgrounds.append(background)

        title_screen_text = Text(
            text = "Progress Bar Test",
            font = G.am.getFont("Garmond",36),
            xy = (G.gameWidth//2,G.gameHeight*3//4),
            halign = "center",
            color = (255,)*3,
        )
        G.objects.append(title_screen_text)

        progress_bar = ProgressBar(
            width = G.gameWidth*6//8,
            height = G.gameHeight//16,
            progress = 0.25,
            xy = (G.gameWidth//2,G.gameHeight*5//8),
            barColor = pygame.Color(64,128,255)
        )
        G.objects.append(progress_bar)
