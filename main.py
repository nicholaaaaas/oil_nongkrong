from __future__ import annotations
from typing import Optional, Tuple
from oil import Oil
from plates import Plates
from experiment import Experiment
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
    _oil_drop: Optional[Oil]
    _plates: Optional[Plates]
    _experiment: Optional[Experiment]

    def __init__(self) -> None:
        """
        Initialize variables for this Game instance
        """
        # basic inits
        self.width, self.height = 1000, 750
        self.size = (self.width, self.height)
        self._running = True
        self.screen = pygame.display.set_mode(self.size)
        
        # gui inits
        self.manager = pygame_gui.UIManager(self.size)
        self.clock = pygame.time.Clock()
        self.slider = pygame_gui.elements.UIHorizontalSlider(
            relative_rect=pygame.Rect(670,500,300,20),manager=self.manager,
            start_value=0, value_range=(0,25000))
        self.textBox = pygame_gui.elements.UILabel(relative_rect=pygame.Rect(670,520,300,20),
            text="Volt: 0", manager=self.manager)
        
        # experiment object inits
        self._oil_drop = None
        self._plates = None
        self._experiment = None

    def setup(self):
        """ Sets up screen and simulation objects. """
        self.screen.fill((190, 180, 164))
        pygame.display.flip()

        # setup the slider to have the value 0
        self.slider.set_current_value(0)

        # sprites
        self._metal_plate = utils.convertPNG(METAL_PLATE, (600, 50))
        self.screen.blit(self._metal_plate, (30, 10))
        self.screen.blit(self._metal_plate, (30, 690))

        # TODO : reset the experiment for each trial
        self._oil_drop = Oil(1.6e-17, 8e-19, 375, 0)
        self._plates = Plates(0.05)  # start with 0V
        self._plates.set_pd(10.8)
        self._experiment = Experiment(self._plates, self._oil_drop)

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
        self._experiment.update()

    def _events(self) -> None:
        """
        Event handling of the game window
        """

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self._running = False
            elif event.type == pygame.MOUSEBUTTONUP:
                pass      
            self.manager.process_events(event)
        self.textBox.set_text("Volt: {}".format(self.slider.get_current_value()/100))
        self.manager.update(self._time_delta)

    def _draw(self) -> None:
        """
        Draws the sprite images to the screen.
        """
        # TODO : Implement
        self.manager.draw_ui(self.screen)

        self.screen.fill((190, 180, 164))
        self.screen.blit(self._metal_plate, (30, 10))
        self.screen.blit(self._metal_plate, (30, 690))
        self._oil_drop.draw(self.screen)

        pygame.display.update()


if __name__ == "__main__":
    pygame.init()
    simulation = Simulation()
    simulation.setup()
    simulation.run()




    