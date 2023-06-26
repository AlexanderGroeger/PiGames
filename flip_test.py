import pygame
pygame.init()

import argparse
parser = argparse.ArgumentParser(
    prog='Display Flip Experiment',
    description='Really bare bones program to test pygame.display.flip')
parser.add_argument('--fullscreen',
                    action='store_true')  # on/off flag
parser.add_argument('--scaled',
                    action='store_true')  # on/off flag
args = parser.parse_args()

use_scaled = args.scaled
use_fullscreen = args.fullscreen

game_width, game_height = 512, 288
fps = 60
color_red, color_blue = (64,16,16), (16,16,64)
scale_factor = 5

flags = pygame.NOFRAME

if use_fullscreen:
    flags |= pygame.FULLSCREEN
    
if use_scaled:
    scale_factor = 1
    flags |= pygame.SCALED

screen = pygame.display.set_mode((game_width*scale_factor, game_height*scale_factor), flags)
screen.set_alpha(None)
appsurf = pygame.Surface((game_width,game_height))
clock = pygame.time.Clock()

while True:
    
    keys = pygame.key.get_pressed()
    for event in pygame.event.get():
        # Close game when escape is pressed
        if keys[pygame.K_ESCAPE]:
            pygame.quit()
            exit()
    
    if use_scaled:
        screen.fill(color_red)
    else:
        appsurf.fill(color_blue)
        pygame.transform.scale_by(appsurf, scale_factor, screen)
        
    pygame.display.flip()    
    clock.tick(fps)