from __future__ import annotations
from typing import Optional, Tuple
import pygame
import utils

FPS = 60
METAL_PLATE = 'assets/metal_plate.png'


class Simulation:
    """
    Class representing the simulation.
    """
    size: Tuple[int, int]
    width: int
    height: int
    screen: Optional[pygame.Surface]

    _running: bool
    _metal_plate: pygame.Surface

    def __init__(self) -> None:
        """
        Initialize variables for this Game instance
        """
        self.width, self.height = 1000, 750
        self.size = (self.width, self.height)
        self.screen = None
        self._running = True

    def setup(self):
        """ Sets up screen and simulation objects. """
        self.screen = pygame.display.set_mode(self.size)
        self.screen.fill((190, 180, 164))
        pygame.display.flip()

        # sprites
        self._metal_plate = utils.convertPNG(METAL_PLATE, (600, 50))
        self.screen.blit(self._metal_plate, (30, 10))
        self.screen.blit(self._metal_plate, (30, 690))

    def run(self) -> None:
        """
        Run the Game until it ends or player quits.
        """
        while self._running:
            # pygame.time.wait(1000 // FPS)
            # set background color

            self._events()
            self._update()
            self._draw()

    def _update(self) -> None:
        """
        Updates object positions and/or properties.
        """
        pass  # TODO

    def _events(self) -> None:
        """
        Event handling of the game window
        """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self._running = False
            elif event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
                print(pos)

    def _draw(self) -> None:
        """
        Draws the sprite images to the screen.
        """
        # TODO : Implement

        pygame.display.flip()


if __name__ == "__main__":
    simulation = Simulation()
    simulation.setup()
    simulation.run()




