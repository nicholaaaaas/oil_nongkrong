from __future__ import annotations
from typing import Optional, Tuple
import pygame
import pygame_gui
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
    manager: pygame_gui.UIManager
    slider: pygame_gui.elements.UIHorizontalSlider
    clock: pygame.time.Clock
    _time_delta: float

    _running: bool
    _metal_plate: pygame.Surface

    def __init__(self) -> None:
        """
        Initialize variables for this Game instance
        """
        self.width, self.height = 1000, 750
        self.size = (self.width, self.height)
        self._running = True
        self.screen = pygame.display.set_mode(self.size)
        self.manager = pygame_gui.UIManager(self.size)
        self.clock = pygame.time.Clock()
        self.slider = pygame_gui.elements.UIHorizontalSlider(
            relative_rect=pygame.Rect(0,0,500,50),manager=self.manager,
            start_value=0, value_range=(0,100))
 

    def setup(self):
        """ Sets up screen and simulation objects. """
        self.screen.fill((190, 180, 164))
        pygame.display.flip()

        # setup the slider to have the value 0
        self.slider.set_current_value = 0

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
            self._time_delta = self.clock.tick(60)/1000.0
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
            self.manager.process_events(event)
        self.manager.update(self._time_delta)

    def _draw(self) -> None:
        """
        Draws the sprite images to the screen.
        """
        # TODO : Implement
        self.manager.draw_ui(self.screen)

        pygame.display.flip()


if __name__ == "__main__":
    pygame.init()
    simulation = Simulation()
    simulation.setup()
    simulation.run()




    