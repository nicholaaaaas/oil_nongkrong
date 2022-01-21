import pygame


class Oil:
    mass: float
    charge: float
    position: float
    velocity: float

    def __init__(self, mass, charge, position, velocity) -> None:
        self.mass = mass
        self.charge= charge
        self.position = position
        self.velocity = velocity

    def draw(self, screen: pygame.Surface) -> None:
        """
        Draws the oil onto the <screen>.
        """
        # TODO : resolve the representation scale
        pass
