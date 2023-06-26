import pygame
if __name__ == "__main__":
    pygame.init()
    flags = pygame.RESIZABLE | pygame.SCALED
    # flags = pygame.RESIZABLE
    pygame.display.set_mode((512, 288), flags)
    pygame.display.set_caption("render")
    print(pygame.display.Info())
    print(pygame.display.get_driver())
    info = pygame.display._get_renderer_info()
    if info is not None:
        r_name, r_flags = info
        print("renderer:", r_name, "flags:", bin(r_flags))
        for flag, name in [(1, "software"), (2, "accelerated"), (4, "VSync"), (8, "render to texture")]:
            if flag & r_flags:
                print(name)
