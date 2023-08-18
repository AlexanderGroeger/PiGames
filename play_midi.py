import pygame
pygame.init()

filepath = "C:\\Users\\alex\\Music\\Zelda\\OracleOfAges\\Overworld.mid"
soundfont = "C:\\Users\\alex\\GamesAndDev\\SoundFonts\\Gameboy_GM_Soundfont_2_.SF2"
pygame.mixer.music.load(filepath)
pygame.mixer.music.play()

screen = pygame.display.set_mode((256, 160))
screen.set_alpha(None)
clock = pygame.time.Clock()

while True:

    keys = pygame.key.get_pressed()
    for event in pygame.event.get():
        # Close game when escape is pressed
        if keys[pygame.K_ESCAPE]:
            pygame.quit()
            exit()

    pygame.display.flip()
    clock.tick(10)
