from __future__ import annotations

from typing import Dict, List, Optional, Tuple
from oil import Oil
from plates import Plates
from experiment import Experiment
from UI import UI
import pygame

import physics_equations as phy
import utils
from UI import UI
from experiment import Experiment
from oil import Oil
from plates import Plates

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
    _mass_dict: Dict[float, Tuple[float, float]]

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
        self.clock = pygame.time.Clock()
        pygame.display.set_caption("Oil Nongkrong -- Millikan's Oil Experiment")

        # experiment objects
        self._oil_drop = Oil(1.6e-17, 8e-19, 320, 0)
        self._plates = Plates(0.05)  # start with 0V
        self._plates.set_pd(0)
        self._experiment = Experiment(self._plates, self._oil_drop)
        self._mass_dict = {8.0e-17: (1.6e-19, 247), 6.4e-17: (3.2e-19, 91),
                           4.8e-17: (4.799e-19, 55), 3.2e-17: (6.4e-19, 30), 1.6e-17: (8e-19, 6)}
        self._ui = UI(self.size, self._plates.dist)

    def setup(self):
        """ Sets up screen and simulation objects. """
        self._frame_count = 0

        self.screen.fill((190, 180, 164))
        pygame.display.flip()

        # sprites
        self._metal_plate = utils.convertPNG(METAL_PLATE, (600, 50))
        self.screen.blit(self._metal_plate, (30, 10))
        self.screen.blit(self._metal_plate, (30, 710))

        # reset experiment objects
        oil_mass = self._ui.get_selected_mass()
        self._oil_drop = Oil(oil_mass, self._mass_dict[oil_mass][0], 375, 0)
        self._plates = Plates(0.05)  # start with 0V
        self._plates.set_pd(self._mass_dict[oil_mass][1])
        self._experiment = Experiment(self._plates, self._oil_drop)

        # UI
        self._ui.ui_setup(self._plates.get_pd() * 100)

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
        self._plates.set_pd(self._ui.read_slider() / 100)
        self._experiment.update(self._time_delta)
        self._ui.ui_update(self._time_delta, self.setup, self._calc_corresponding_charge,
                           self._oil_drop.mass, self._oil_drop.velocity,
                           self._experiment.get_accel())

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
            self._ui.update_slider(direction)
            self._frame_count = 5
        else:
            self._frame_count -= 1

        if self._ui.get_selected_mass() != self._oil_drop.mass:
            self.setup()

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

    def _calc_corresponding_charge(self) -> float:
        """ Return the corresponding charge given the current voltage
            set, assuming the acceleration is 0.

            This used to simulate an actual calculation where the exact
            acceleration at a given time is not known.
        """
        return phy.charge_oil(self._oil_drop.mass, 0, self._plates.dist,
                              self._plates.get_pd())


if __name__ == "__main__":
    pygame.init()
    simulation = Simulation()
    simulation.setup()
    simulation.run()
