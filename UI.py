from __future__ import annotations
from typing import Callable, List, Optional, Tuple, Union

import pygame
import pygame_gui
import utils

EQ_PATH = "assets/pyjac_equations.png"


class UI:
    """ A class responsible for managing the UI. """
    _manager: pygame_gui.UIManager
    _slider: pygame_gui.elements.UIHorizontalSlider
    _new_btn: pygame_gui.elements.UIButton

    # labels
    _mass_label: pygame_gui.elements.UILabel
    _velocity_label: pygame_gui.elements.UILabel
    _acceleration_label: pygame_gui.elements.UILabel
    _distance_label: pygame_gui.elements.UILabel
    _pd_label: pygame_gui.elements.UILabel

    _mass_list: pygame_gui.elements.UIDropDownMenu

    _charge_calc: pygame_gui.elements.UILabel

    _equations: Optional[pygame.Surface]
    _instructions: List[Union[pygame.Surface, pygame.SurfaceType]]

    def __init__(self, size: Tuple[int, int], dist: float) -> None:
        """ Initialize the UI with screen size <size>
            and plate separation <dist>.
        """
        self._manager = pygame_gui.UIManager(size)
        self._slider = pygame_gui.elements.UIHorizontalSlider(
            relative_rect=pygame.Rect(670, 620, 300, 20), manager=self._manager,
            start_value=0, value_range=(0, 25000))

        self._mass_label = pygame_gui.elements.UILabel(
            relative_rect=pygame.Rect(670, 520, 300, 20),
            text="Mass (kg): 0", manager=self._manager)
        self._velocity_label = pygame_gui.elements.UILabel(
            relative_rect=pygame.Rect(670, 540, 300, 20),
            text="Velocity (m/s): 0", manager=self._manager)
        self._acceleration_label = pygame_gui.elements.UILabel(
            relative_rect=pygame.Rect(670, 560, 300, 20),
            text="Acceleration (m/s^2): 0", manager=self._manager)
        self._distance_label = pygame_gui.elements.UILabel(
            relative_rect=pygame.Rect(670, 580, 300, 20),
            text=f"Plate separation (m): {dist}", manager=self._manager)
        self._pd_label = pygame_gui.elements.UILabel(
            relative_rect=pygame.Rect(670, 600, 300, 20),
            text="Potential Difference (V): 0", manager=self._manager)

        self._new_btn = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect(770, 670, 100, 50),
            text="Reset", manager=self._manager)

        self._mass_list = pygame_gui.elements.UIDropDownMenu(relative_rect=pygame.Rect(
            720, 350, 200, 20), starting_option="1.6e-17", manager=self._manager, 
            options_list=["8.0e-17", "6.4e-17", "4.8e-17", "3.2e-17", "1.6e-17"])

        # calculations
        self._equations = None
        self._charge_calc = pygame_gui.elements.UILabel(
            relative_rect=pygame.Rect(670, 380, 300, 20),
            text="Charge (C): --", manager=self._manager)
        self._calc_btn = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect(775, 420, 100, 50),
            text="Calculate", manager=self._manager)

        # instructions
        font = pygame.font.SysFont("timesnewroman", 20)
        instructions = ["1. Choose a mass and adjust the potential"
                        " difference until acceleration is 0",
                        "2. Once you have the right potential difference,",
                        "    hit calculate to find the corresponding charge."]
        white = (0, 0, 0)
        self._instructions = [font.render(inst, True, white) for inst in
                              instructions]

    def ui_setup(self, slider_initial: float) -> None:
        """ Handles all the UI setup.

            slider_initial: the initial value for the p.d. slider
        """
        self._slider.set_current_value(slider_initial)
        self._equations = utils.convertPNG(EQ_PATH, (300, 300))

    def ui_update(self, time_delta: float, reset_callback: Callable,
                  calculate_callback: Callable,
                  mass: float, velocity: float, acc: float) -> None:
        """ Handles all the UI updates. """
        if self._new_btn.check_pressed():
            reset_callback()
            self.ui_setup(0)

        if self._calc_btn.check_pressed():
            corresponding_charge = calculate_callback()
            self._charge_calc.set_text("Charge (C): "
                                       f"{corresponding_charge:.2e}")

        self._pd_label.set_text(
            "Potential Difference (V): "
            f"{self._slider.get_current_value() / 100}")
        self._mass_label.set_text(
            f"Mass (kg): {mass}")
        self._velocity_label.set_text(
            f"Velocity (m/s): {velocity:.2f}")
        self._acceleration_label.set_text(
            f"Acceleration (m/s^2): {acc:.2f}")

        self._manager.update(time_delta)

    def process_events(self, event: pygame.Event) -> None:
        """ Handles all UI events. """

        self._manager.process_events(event)

    def update_slider(self, value: int) -> None:
        """ Increments the slider by <value>.

            Note: this method fails silently if the <value> will cause
                slider to exceed its range.
         """
        self._slider.set_current_value(
            self._slider.get_current_value() + value)

    def read_slider(self) -> int:
        """ Reads the value from the slider. """
        return self._slider.get_current_value()

    def draw_ui(self, screen: pygame.Surface) -> None:
        """ Draw the UI to the screen. """
        self._manager.draw_ui(screen)
        screen.blit(self._equations, (670, 80))
        for i, inst in enumerate(self._instructions):
            screen.blit(inst, (670, 10 + i * 20))

    def get_selected_mass(self)-> float:
        """ Return the mass selected. """
        return float(self._mass_list.selected_option)
        
