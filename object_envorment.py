import pygame as pg


class Tree(pg.sprite.Sprite):
    def __init__(self, x, y):
        pg.sprite.Sprite.__init__(self)

        self.image = pg.image.load('assets/tree.png').convert_alpha()
        self.image = pg.transform.scale(self.image, (480, 480))
        self.rect = self.image.get_rect()

        self.rect.centerx = x
        self.rect.centery = y
