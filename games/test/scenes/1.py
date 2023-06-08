from pygame import mixer

from lib.scene import Scene
from lib.background import Background, ScrollingBackground
from lib.text import Text

import lib.globals as G

class Main(Scene):

    def __init__(self):
        Scene.__init__(self)

    def start(self):
        G.am.loadMusic("run")
        mixer.music.play(-1)
        for (i, s) in zip(range(4,0,-1),(1,2,4,6)):
            dark_forest_background = ScrollingBackground(
                img = G.am.getGraphic(f"background/dark_forest/{i}",alpha=True),
                hspeed = -s,
                wrap = True
            )
            G.backgrounds.append(dark_forest_background)
