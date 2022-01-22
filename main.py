from __future__ import annotations

from typing import Optional, Tuple
from oil import Oil
from plates import Plates
from experiment import Experiment
from UI import UI
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
    clock: pygame.time.Clock

    _ui: UI
    _time_delta: float
    _running: bool
    _metal_plate: pygame.Surface
    _oil_drop: Optional[Oil]
    _plates: Optional[Plates]
    _experiment: Optional[Experiment]
    _frame_count: int

    def __init__(self) -> None:
        """
        Initialize variables for this Game instance
        """
        # basic init
        self.width, self.height = 1300, 750
        self.size = (self.width, self.height)
        self._running = True
        self._frame_count = 0
        self.screen = pygame.display.set_mode(self.size)
<<<<<<< HEAD
        self.clock = pygame.time.Clock()

        self._ui = UI(self.size)
=======

        # gui init
        self.manager = pygame_gui.UIManager(self.size)
        self.clock = pygame.time.Clock()
        self.slider = pygame_gui.elements.UIHorizontalSlider(
            relative_rect=pygame.Rect(670, 550, 300, 20), manager=self.manager,
            start_value=0, value_range=(0, 25000))
        self.textBox = pygame_gui.elements.UILabel(
            relative_rect=pygame.Rect(670, 570, 300, 20),
            text="Volt (V): 0", manager=self.manager)
        self.new_btn = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect(770, 620, 100, 50),
            text="New", manager=self.manager)

        # experiment object init
>>>>>>> main
        self._oil_drop = None
        self._plates = None
        self._experiment = None

    def setup(self):
        """ Sets up screen and simulation objects. """
        self._frame_count = 0

        self.screen.fill((190, 180, 164))
        pygame.display.flip()

        # sprites
        self._metal_plate = utils.convertPNG(METAL_PLATE, (600, 50))
        self.screen.blit(self._metal_plate, (30, 10))
        self.screen.blit(self._metal_plate, (30, 710))

        # experiment objects
        self._oil_drop = Oil(1.6e-17, 8e-19, 375, 0)
        self._plates = Plates(0.05)  # start with 0V
        self._plates.set_pd(0)
        self._experiment = Experiment(self._plates, self._oil_drop)

<<<<<<< HEAD
        # UI
        self._ui.ui_setup(self._plates.get_pd() * 100)

=======
>>>>>>> main
    def run(self) -> None:
        """
        Run the Game until it ends or player quits.
        """
        while self._running:
            # set background color
            self._time_delta = self.clock.tick(60) / 1000.0
            self._events()
            self._update()
            self._draw()

    def _update(self) -> None:
        """
        Updates object positions and/or properties.
        """
<<<<<<< HEAD
        self._plates.set_pd(self._ui.get_slider().get_current_value() / 100)
        self._experiment.update(self._time_delta)
        self._ui.ui_update(self._time_delta)
=======
        self._plates.set_pd(self.slider.get_current_value() / 100)
        self.textBox.set_text(f"Volt (V): {self._plates.get_pd()}")
        self.manager.update(self._time_delta)
        self._experiment.update(self._time_delta)

        if self.new_btn.check_pressed():
            self.setup()
>>>>>>> main

    def _events(self) -> None:
        """
        Event handling of the game window
        """

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self._running = False
            self._ui.process_events(event)

        # limit to moving once every ten frames
        if self._frame_count == 0:
            # get arrow input
            keys = pygame.key.get_pressed()
            # 1 if right(+) direction,
            # 0 if no press or both pressed,
            # -1 if left(-) direction
            direction = keys[pygame.K_RIGHT] - keys[pygame.K_LEFT]
<<<<<<< HEAD
            self._ui.get_slider().set_current_value(
                self._ui.get_slider().get_current_value() + direction)
=======
            self.slider.set_current_value(self.slider.get_current_value()
                                          + direction)
>>>>>>> main
            self._frame_count = 9
        else:
            self._frame_count -= 1

    def _draw(self) -> None:
        """
        Draws the sprite images to the screen.
        """
        self.screen.fill((190, 180, 164))
        self.screen.blit(self._metal_plate, (30, 10))
        self.screen.blit(self._metal_plate, (30, 690))
        self._oil_drop.draw(self.screen)

        self._ui.draw_ui(self.screen)
        pygame.display.update()


if __name__ == "__main__":
    pygame.init()
    simulation = Simulation()
    simulation.setup()
    simulation.run()
