from typing import Optional

import pygame
import random

from people import Man, Woman

# Constants
WIDTH = 1200
HEIGHT = 700

GREEN = (0, 255, 0)

# Initiation pygame
pygame.init()


def main():
    # Create vars and functions
    # Create vars screen size
    width = WIDTH
    height = HEIGHT

    idef = 2

    # Create var screen
    screen = pygame.display.set_mode((width, height))

    # Set up caption
    pygame.display.set_caption("")

    # Create group object
    group: Optional[pygame.sprite.Group] = pygame.sprite.Group()

    # Create first peoples
    people_0: Optional[pygame.sprite] = Man(width // 2, height // 2, 0)
    people_1: Optional[pygame.sprite] = Woman(width // 2, height // 2, 1)
    # Append in group
    group.add(people_0, people_1)

    x = y = 0

    # Function update people
    def update_people(pl, x, y):
        pl.update(screen)
        pl.rect.x += x // 2
        pl.rect.y += y // 2
    # Game loop
    while 1:
        # FPS
        pygame.time.Clock().tick(60)

        # Create a random reproduction
        f = random.randint(1, 50)
        if f == 1:
            idef += 1

            f1 = random.randint(1, 2)
            if f1 == 1:
                d: Optional[pygame.sprite] = Man(width // 2, height // 2, idef)
                group.add(d)
            if f1 == 2:
                d: Optional[pygame.sprite] = Woman(width // 2, height // 2, idef)
                group.add(d)

        # Check events
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                raise SystemExit
            if e.type == pygame.MOUSEBUTTONDOWN:
                pygame.mouse.get_rel()
            if e.type == pygame.MOUSEBUTTONUP:
                x, y = pygame.mouse.get_rel()

        group.draw(screen)
        pygame.display.update()
        screen.fill(GREEN)

        for pl in group:
            update_people(pl, x, y)
        x = y = 0


if __name__ == "__main__":
    main()
