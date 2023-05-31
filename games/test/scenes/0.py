from pygame import mixer

from lib.scene import Scene
from lib.background import Background, ScrollingBackground
from lib.text import Text
from lib.menu import LinearTextMenu
from lib.animation import Infinity

import lib.globals as G

class Main(Scene):

    def __init__(self):
        super().__init__()

    def start(self):
        G.am.loadMusic("title")
        mixer.music.play(-1)

        dark_forest_background = Background(
            img = G.am.getGraphic(f"background/dark_forest/compiled")
        )
        G.backgrounds.append(dark_forest_background)

        title_screen_text = Text(
            text = "Text Quest",
            font = G.am.getFont("Garmond",36),
            xy = (G.gameWidth//4,G.gameHeight//16),
            halign = "center",
            color = (255,)*3,
        )
        G.objects.append(title_screen_text)

        main_menu = LinearTextMenu(
            {
                "Play": lambda: G.sm.goToScene(1),
                "Settings": False,
                "Exit": lambda: G.game.exit()
            },
            vspace = G.gameHeight//8,
            # hspace = G.gameWidth//4,
            # halign = 'center',
            alphaDim = 64,
            selectedAnimation = Infinity(width=14,height=8,seconds_per_cycle=2),
            font = G.am.getFont("Garmond",24),
            xy = (G.gameWidth//8,G.gameHeight//4),
            color = (255,)*3,
            # vertical = False,
        )
        G.objects.append(main_menu)
