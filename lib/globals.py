import pygame

def init():
    global windowWidth, windowHeight, gameWidth, gameHeight
    pygame.display.init()
    windowWidth, windowHeight = pygame.display.get_desktop_sizes()[0]
    global windowFullScreen
    windowFullScreen = False
    # windowWidth, windowHeight = (1920, 1080)
    gameWidth, gameHeight = windowWidth, windowHeight

    global fps
    fps = 60

    global t
    t = 0

    global gameDir

    global backgrounds, objects
    backgrounds = []
    objects = []

    global controllers
    controllers = dict()
