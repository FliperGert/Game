import pygame
import re


def convert(old_file, name):
    pygame.image.save(old_file, f'save/{name}.png')


def transform(old_file, size):
    return pygame.transform.scale(old_file, size)


def finish_con(file, size, new_name):
    file = transform(file, size)
    convert(file, new_name)


file = pygame.image.load('load/p22.jpeg')
finish_con(file, (512, 512), f'p24')
