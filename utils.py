from typing import Optional, Tuple

import pygame


def convertPNG(path: str,
               scale: Optional[Tuple[int, int]] = None) -> pygame.Surface:
    obj = pygame.image.load(path).convert_alpha()
    if scale is not None:
        obj = pygame.transform.scale(obj, scale)
    return obj
