from typing import Optional

import pygame
import random

from people import Man, Woman
from object_envorment import Tree

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

    # Create system time
    time = 0

    # Create var screen
    screen = pygame.display.set_mode((width, height))

    # Set up caption
    pygame.display.set_caption("")

    # Create group object
    group: Optional[pygame.sprite.Group] = pygame.sprite.Group()

    # Create first peoples
    people_0: Optional[pygame.sprite] = Man(width // 2, height // 2, 0,  20)
    people_1: Optional[pygame.sprite] = Woman(width // 2, height // 2, 1, 10)
    # Append in group
    group.add(people_0, people_1)

    # Create tree
    tree: Optional[pygame.sprite] = Tree(width // 2, height // 2)
    group.add(tree)
    x = y = 0

    # Game loop
    while 1:
        # FPS
        pygame.time.Clock().tick(60)

        # Create a random reproduction
        if len(group) < 5:
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
            pl.update(screen)
            pl.rect.x += x // 2
            pl.rect.y += y // 2
        x //= 2
        y //= 2

        time += 1
        print(time)


if __name__ == "__main__":
    main()
