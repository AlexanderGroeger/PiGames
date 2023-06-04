# Use faster alpha blending!
import os
os.environ['PYGAME_BLEND_ALPHA_SDL2'] = "1"

import pygame
pygame.init()
from sys import exit

import lib.globals as G
from lib.assetManager import AssetManager
from lib.moduleManager import ModuleManager
from lib.input.controller import controller_guids, Controller

G.am = AssetManager()
G.mm = ModuleManager()
G.keys = pygame.key.get_pressed()

class Game():

    def __init__(self):

        pygame.display.set_caption("PyGame")
        flags = pygame.FULLSCREEN | pygame.SCALED | pygame.NOFRAME
        self.screen = pygame.display.set_mode((G.gameWidth, G.gameHeight),flags=flags)
        self.screen.set_alpha(None)
        self.bgcolor = (0,)*3
        self.appsurf = pygame.Surface((G.gameWidth,G.gameHeight))

        # G.gameScale = min(G.windowWidth//G.gameWidth,G.windowHeight//G.gameHeight)
        # G.gameScaledWidth, G.gameScaledHeight = G.gameWidth*G.gameScale, G.gameHeight*G.gameScale
        # G.gameDeltaX, G.gameDeltaY = (G.windowWidth-G.gameScaledWidth)//2, (G.windowHeight-G.gameScaledHeight)//2

    def run(self):

        self.clock = pygame.time.Clock()

        while True:

            self.input()
            self.step()
            self.draw()

            # Upscale game resolution to fit screen
            # self.screen.blit(pygame.transform.scale_by(self.appsurf,G.gameScale),(G.gameDeltaX, G.gameDeltaY))
            self.screen.blit(self.appsurf,(0,0))

            # Draw screen
            pygame.display.flip()

            G.t += 1
            self.clock.tick(G.fps)

    def input(self):

        # Check keys pressed
        G.keys = pygame.key.get_pressed()

        G.events = pygame.event.get()
        for event in G.events:
            # Close game when window X button is pressed
            if event.type == pygame.QUIT:
                self.exit()

            # Handle hotplugging
            if event.type == pygame.JOYDEVICEADDED:
                # This event will be generated when the program starts for every
                # joystick, filling up the list without needing to create them manually.

                joy = pygame.joystick.Joystick(event.device_index)
                G.controllers[str(joy.get_instance_id())] = controller_guids.get(event.__dict__.get("guid"), Controller)(joy)
                print(f"Joystick {joy.get_instance_id()} connencted")

            if event.type == pygame.JOYDEVICEREMOVED:
                del G.joysticks[event.instance_id]
                print(f"Joystick {event.instance_id} disconnected")

        # Close game when escape is pressed
        if G.keys[pygame.K_ESCAPE]:
            self.exit()

        for obj in G.objects:
            if getattr(obj,'input',None):
                obj.input()

        for instance_id, controller in G.controllers.items():
            controller.input()


    def step(self):
        for bg in G.backgrounds:
            bg.step()
        G.objects.sort(key = lambda x: int(getattr(x,'depth',0)))
        for obj in G.objects:
            obj.step()

    def draw(self):

        self.appsurf.fill(self.bgcolor)

        # Draw background layers
        for bg in G.backgrounds:
            bg.draw(self.appsurf)

        # Draw objects
        for obj in G.objects:
            obj.draw(self.appsurf)



    def exit(self):
        pygame.quit()
        exit()
