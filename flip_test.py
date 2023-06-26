import pygame
pygame.init()
import sys
use_scaled = len(sys.argv)==1
if use_scaled:
    flags = pygame.SCALED
else:
    flags = 0

screen = pygame.display.set_mode((512*(4-3*int(use_scaled)), 288*(4-3*int(use_scaled))), flags)
screen.set_alpha(None)
appsurf = pygame.Surface((512,288))
clock = pygame.time.Clock()

while True:
    
    for event in pygame.event.get():
        # Close game when window X button is pressed
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    
    if use_scaled:
        screen.fill((64,48,16))
    else:
        appsurf.fill((16,48,64))
        pygame.transform.scale_by(appsurf, 4, screen)
        
    pygame.display.flip()    
    clock.tick(60)