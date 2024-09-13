from colorsys import yiq_to_rgb
from typing import Optional

import pygame
import pygame_gui as pu
import random

from Cython.Compiler.Nodes import relative_position

from people import Man, Woman
from object_envorment import Tree

# Constants
WIDTH = 1200
HEIGHT = 600

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

    # Create type camera
    camera_focus = False

    # Create system time
    time = 0

    # Create var screen
    screen = pygame.display.set_mode((width, height))
    # Create background
    background = pygame.Surface((800, 600))
    background.fill(pygame.Color('#000000'))

    # Create UI manager
    manager = pu.UIManager((width, height), theme_path='button.json')

    # Set up caption
    pygame.display.set_caption("")

    # Create group object
    group: Optional[pygame.sprite.Group] = pygame.sprite.Group()
    people = []
    objects = []

    # Create system reproduction
    child = []
    men = []
    women = []
    parents = {}

    # Create first peoples
    people_0: Optional[pygame.sprite] = Man(width // 2, height // 2, 0,[],20)
    people_1: Optional[pygame.sprite] = Woman(width // 2, height // 2, 1, [],18)
    # Add how child
    child.extend([people_0, people_1])
    # Append in group
    group.add(people_0, people_1)
    people.extend([people_0, people_1])

    # Create tree
    tree: Optional[pygame.sprite] = Tree(width // 2, height // 2)
    group.add(tree)
    objects.append(tree)

    # Create button
    menu_button = pu.elements.UIButton(pygame.Rect((10, 10), (50, 50)), "=", manager)

    return_button = pu.elements.UIButton(pygame.Rect((10, 10), (150, 50)), "return", manager)
    return_button.hide()
    setting_button = pu.elements.UIButton(pygame.Rect((10, 70), (150, 50)), "settings", manager)
    setting_button.hide()
    exit_button = pu.elements.UIButton(pygame.Rect((10, 130), (150, 50)), "exit", manager)
    exit_button.hide()

    x_m = y_m = y_k = x_k = x_vel = y_vel = 0

    # Game loop
    while 1:
        # FPS
        pygame.time.Clock().tick(60)

        # Check child
        for ch in child:
            if ch.year >= 18:
                if isinstance(ch, Man):
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

            # Check pare
            if w.pare and not w.pregnant:
                if random.randint(1, 1000) == 100:
                    w.pregnant = True
                    print('yes')

            # Check pregnant women
            if w.birth:
                match random.randint(1, 3):
                    case 1:
                        people: Optional[pygame.sprite] = Woman(w.rect.centerx, w.rect.centery, idef,
                                                                [w.get_name(), w.gay])
                        idef += 1
                        group.add(people)
                        child.append(people)
                    case 2:
                        people: Optional[pygame.sprite] = Man(w.rect.centerx, w.rect.centery, idef,
                                                                [w.get_name(), w.gay])
                        idef += 1
                        group.add(people)
                        child.append(people)
                    case _:
                        pass
                w.birth = False
                w.pregnant = False

        # Check events
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                raise SystemExit

            if e.type == pygame.MOUSEBUTTONDOWN:
                for pl in people:
                    pl.focused()
                pygame.mouse.get_rel()
            if e.type == pygame.MOUSEBUTTONUP:
                x_m, y_m = pygame.mouse.get_rel()

            # Power off focus
            if e.type == pygame.KEYDOWN and e.key == pygame.K_ESCAPE:
                camera_focus = False
                for pl in people:
                    pl.focus = False

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

            # Check menu button
            if e.type == pu.UI_BUTTON_PRESSED:
                if e.ui_element == menu_button:
                    menu_button.hide()
                    return_button.show()
                    setting_button.show()
                    exit_button.show()

                if e.ui_element == return_button:
                    return_button.hide()
                    setting_button.hide()
                    exit_button.hide()
                    menu_button.show()
                # Create exit and settings
                if e.ui_element == setting_button:
                    screen.blit(background, (0, 0))

                if e.ui_element == exit_button:
                    raise SystemExit

                if e.ui_element == exit_button:
                    raise SystemExit
            # Manager check events
            manager.process_events(e)

        # Manager update
        manager.update(pygame.time.Clock().tick(60) / 1000.0)
        manager.draw_ui(screen)

        # Window update
        group.draw(screen)
        pygame.display.update()
        screen.fill(GREEN)

        for pl in group:
            if pl in people:
                if pl.focus and camera_focus:
                    x_vel = -pl.xvel
                    y_vel = -pl.yvel
                    # Output info
                    info_text = pu.elements.UITextBox(html_text=f'Name: {pl.get_name()}\n'
                                                                f'HP: {pl.live}\n'
                                                                f'Parents: {pl.parents[0]}, {pl.parents[1]}',
                                                      relative_rect=pygame.Rect((0, 2 * height//3), (width//6, height//3)),
                                                      manager=manager)
                if pl.focus and not camera_focus:
                    camera_focus = True
                    x_vel = -(pl.rect.centerx - width // 2)
                    y_vel = -(pl.rect.centery - height // 2)

            # Move camera
            if camera_focus:
                pl.rect.x += x_vel
                pl.rect.y += y_vel
            else:
                pl.rect.x += x_m // 2 + x_k
                pl.rect.y += y_m // 2 + y_k
            pl.update(screen)

        # Slow camera for mouse
        if x_m == 1: x_m = 0
        x_m //= 2
        if y_m == 1: y_m = 0
        y_m //= 2

        # Slow focus camera
        x_vel = 0
        y_vel = 0

        # Time update
        time += 1


if __name__ == "__main__":
    main()
