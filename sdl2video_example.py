import pygame
import pygame._sdl2 as pg_sdl2  # noqa
from pygame._sdl2 import Texture

import numpy as np

WIDTH, HEIGHT = 3440//4, 1440//4
FPS = 60

pygame.init()
# screen = pygame.display.set_mode((WIDTH, HEIGHT), flags=pygame.NOFRAME | pygame.SCALED)
clock = pygame.Clock()

window = pg_sdl2.Window(title="test", size=(WIDTH,HEIGHT), fullscreen_desktop=True)
# window = pg_sdl2.Window.from_display_module()
renderer = pg_sdl2.Renderer(window,vsync=True)
renderer.scale = (4,4)
to_texture = lambda surf: Texture.from_surface(renderer,surf)
clear = renderer.clear
update = renderer.present

surf = pygame.Surface((64, 64))
surf.fill("red")
text = to_texture(surf)
dst_rect = surf.get_rect(center=(WIDTH / 2, HEIGHT / 2))

angle = 0
running = True
while running:
    clock.tick(FPS)
    clear()

    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT or event.type == pygame.KEYDOWN:
            running = False

    angle = (angle + 1) % 180

    text.draw(dstrect=dst_rect.move(512*(abs(angle-90)-45)/90,0),angle=2*angle)

    update()
