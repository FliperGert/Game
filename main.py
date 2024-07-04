import pygame
from people import People

from typing import Optional

# Constants
WIDTH = 600
HEIGHT = 400

GREEN = (0, 255, 0)

# Initiation pygame
pygame.init()


def main():
    # Create vars and functions
    # Create vars screen size
    width = WIDTH
    height = HEIGHT

    # Create var screen
    screen = pygame.display.set_mode((width, height))

    # Set up caption
    pygame.display.set_caption("")

    # Create group object
    group: Optional[pygame.sprite.Group] = pygame.sprite.Group()

    # Create first people
    people_0: Optional[pygame.sprite] = People(width // 2, height // 2)
    # Append in group
    group.add(people_0)

    # Game loop
    while 1:
        # FPS
        pygame.time.Clock().tick(60)

        # Check events
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                raise SystemExit

        group.draw(screen)
        pygame.display.update()
        screen.fill(GREEN)
        people_0.update()


if __name__ == "__main__":
    main()
