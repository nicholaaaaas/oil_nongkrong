from ast import Tuple

import pygame


def convertPNG(path: str, scale: Tuple(int, int)) -> pygame.Surface:
    obj = pygame.image.load(path).convert_alpha()
    obj = pygame.transform.scale(obj, scale)
    return obj
