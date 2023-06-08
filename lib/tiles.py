import pygame

class Tileset:
    
    def __init__(self, file, size=(32, 32), margin=0, spacing=0, alpha=False):
        self.file = file
        self.size = size if type(size) == tuple else (size,)*2
        self.margin = margin
        self.spacing = spacing
        if alpha:
            self.image = pygame.image.load(file).convert_alpha()
        else:
            self.image = pygame.image.load(file).convert()
        self.rect = self.image.get_rect()
        self.tiles = []
        self.load()


    def load(self):

        self.tiles = []
        x0 = y0 = self.margin
        w, h = self.rect.size
        dx = self.size[0] + self.spacing
        dy = self.size[1] + self.spacing

        for x in range(x0, w, dx):
            for y in range(y0, h, dy):
                tile = self.image.subsurface(pygame.Rect((x, y, *self.size)))
                self.tiles.append(tile)

    def __str__(self):
        return f'{self.__class__.__name__} file:{self.file} tile:{self.size}'
