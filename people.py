import pygame as pg
import random


class People(pg.sprite.Sprite):
    def __init__(self, x, y):
        pg.sprite.Sprite.__init__(self)

        # Set up image
        match random.randint(1, 2):
            case 1:
                self.image = pg.image.load("assets/people/people 1.png")
                self.images = [pg.transform.scale(pg.image.load(f"assets/people/people_1_{i}.png"), (56, 64)) for i in range(4)]
            case 2:
                self.image = pg.image.load("assets/people/people 2.png")

        self.image = pg.transform.scale(self.image, (56, 64))

        # Set up hitbox
        self.rect = self.image.get_rect()

        # Set up start coordination
        self.rect.centerx = x
        self.rect.centery = y

        # Create var
        self.run: bool = False
        self.right: bool = False
        self.up: bool = False
        self.down: bool = False
        self.left: bool = False

        self.xvel: int = 0
        self.yvel: int = 0

        self.flip: bool = False

        self.index: int = 0

    def update(self):
        match random.randint(1, 7):
            case 1:
                self.down = True
                self.up = False
            case 2:
                self.up = True
                self.down = False

            case _:
                self.up = self.down = False

        match random.randint(1, 7):
            case 1:
                self.right = True
                self.left = False
            case 2:
                self.left = True
                self.right = False
            case _:
                self.left = self.right = False

        self.move()

    def move(self):
        pg.time.delay(20)
        if self.xvel == 0 and self.yvel == 0:
            if self.run:
                self.rect.x += 2
            else:
                if self.right:
                    self.xvel = 10
                if self.left:
                    self.xvel = -10
                    self.flip = True

                if self.up:
                    self.yvel = 10
                if self.down:
                    self.yvel = -10
        else:
            if self.xvel > 0:
                self.xvel -= 1
            if self.xvel < 0:
                self.xvel += 1
            if self.yvel > 0:
                self.yvel -= 1
            if self.yvel < 0:
                self.yvel += 1

            self.animation()

        self.rect.x += self.xvel
        self.rect.y += self.yvel

    def animation(self):
        if self.index == len(self.images)-1:
            self.index = 0
        else:
            self.index += 1

        for i in range(30):
            if i == 29:
                self.image = self.images[self.index]
            if self.flip:
                self.image = pg.transform.flip(self.image, True, False)
        self.flip = False
