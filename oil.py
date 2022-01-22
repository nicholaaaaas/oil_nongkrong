import pygame
import utils

IMAGE_PATH = "assets/oil.png"



class Oil:
    mass: float
    charge: float
    position: float
    velocity: float

    def __init__(self, mass, charge, position, velocity) -> None:
        self.mass = mass
        self.charge = charge
        self.position = position
        self.velocity = velocity
        self._image = utils.convertPNG(IMAGE_PATH, (30, 30))


    def draw(self, screen: pygame.Surface) -> None:
        """
        Draws the oil onto the <screen>.
        """
        screen.blit(self._image, (320, self.position))
