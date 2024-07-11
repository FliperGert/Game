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
# Limited pygame event(for optimization)
pygame.event.set_allowed([pygame.QUIT, pygame.KEYUP, pygame.KEYDOWN, pygame.MOUSEBUTTONDOWN,
                          pygame.MOUSEBUTTONUP, pygame.MOUSEWHEEL])


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

    # Create system reproduction
    child = []
    men = []
    women = []
    parents = {}

    # Create first peoples
    people_0: Optional[pygame.sprite] = Man(width // 2, height // 2, 0,  20)
    people_1: Optional[pygame.sprite] = Woman(width // 2, height // 2, 1, 18)
    # Add how child
    child.extend([people_0, people_1])
    # Append in group
    group.add(people_0, people_1)

    # Create tree
    tree: Optional[pygame.sprite] = Tree(width // 2, height // 2)
    group.add(tree)
    x_m = y_m = y_k = x_k = 0

    # Game loop
    while 1:
        # FPS
        pygame.time.Clock().tick(60)

        # Check child
        for ch in child:
            print(ch.year)
            if ch.year >= 18:
                if type(ch) == Man:
                    men.append(ch)
                    child.remove(ch)
                    print(men)
                else:
                    women.append(ch)
                    child.remove(ch)
                    print(women)

        # Check women
        for w in women:
            gay = random.choice(men)
            if not w.pare and not gay.pare and random.randint(1, 100) == 69:
                w.pare = gay.pare = True
                w.gay = gay.get_name()
                gay.girl = w.get_name()
                print(w.gay)

        # Check events
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                raise SystemExit
            if e.type == pygame.MOUSEBUTTONDOWN:
                pygame.mouse.get_rel()
            if e.type == pygame.MOUSEBUTTONUP:
                x_m, y_m = pygame.mouse.get_rel()

            # Move camera
            if e.type == pygame.KEYDOWN and e.key == pygame.K_UP:
                y_k += 50
            if e.type == pygame.KEYDOWN and e.key == pygame.K_DOWN:
                y_k += -50
            if e.type == pygame.KEYDOWN and e.key == pygame.K_LEFT:
                x_k += 50
            if e.type == pygame.KEYDOWN and e.key == pygame.K_RIGHT:
                x_k += -50

            if e.type == pygame.KEYUP and e.key == pygame.K_UP:
                y_k = 0
            if e.type == pygame.KEYUP and e.key == pygame.K_DOWN:
                y_k = 0
            if e.type == pygame.KEYUP and e.key == pygame.K_LEFT:
                x_k = 0
            if e.type == pygame.KEYUP and e.key == pygame.K_RIGHT:
                x_k = 0

        group.draw(screen)
        pygame.display.update()
        screen.fill(GREEN)

        for pl in group:
            pl.update(screen)
            # Move camera
            pl.rect.x += x_m // 2 + x_k
            pl.rect.y += y_m // 2 + y_k

        # Slow camera for mouse
        x_m //= 2
        y_m //= 2

        # Time update
        time += 1


if __name__ == "__main__":
    main()
