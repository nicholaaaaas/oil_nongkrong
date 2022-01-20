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
    
    def draw(screen: pygame.surface) -> None:
        """
        Draws the oil onto the <screen>.
        """
        pass
