from __future__ import annotations
from typing import Tuple

import pygame
import pygame_gui


class UI:
    _manager: pygame_gui.UIManager
    _slider: pygame_gui.elements.UIHorizontalSlider
    _new_btn: pygame_gui.elements.UIButton

    # labels
    mass_label: pygame_gui.elements.UILabel
    velocity_label: pygame_gui.elements.UILabel
    acceleration_label: pygame_gui.elements.UILabel
    distance_label: pygame_gui.elements.UILabel
    voltTextBox: pygame_gui.elements.UILabel

    def __init__(self, size: Tuple[int, int]) -> None:
        self._manager = pygame_gui.UIManager(size)
        self._slider = pygame_gui.elements.UIHorizontalSlider(
            relative_rect=pygame.Rect(670, 550, 300, 20), manager=self._manager,
            start_value=0, value_range=(0, 25000))
        self.voltTextBox = pygame_gui.elements.UILabel(
            relative_rect=pygame.Rect(670, 570, 300, 20),
            text="Volt (V): 0", manager=self._manager)
        self._new_btn = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect(770, 620, 100, 50),
            text="New", manager=self._manager)

    def ui_setup(self, slider_initial: float) -> None:
        """ Handles all the UI setup. 
        
            slider_initial: the initial value for the p.d. slider
        """
        self._slider.set_current_value(slider_initial)

    def ui_update(self, time_delta: float) -> None:
        """ Handles all the UI updates. """
        if self._new_btn.check_pressed():
            self.ui_setup()
        self.voltTextBox.set_text(
            f"Volt (V): {self._slider.get_current_value() / 100}")
        self._manager.update(time_delta)

    def process_events(self, event: pygame.Event):
        """ Handles all UI events. """
        self._manager.process_events(event)

    def get_slider(self) -> pygame_gui.elements.UIHorizontalSlider:
        """ Return a reference to the slider. """
        return self._slider

    def draw_ui(self, screen: pygame.Surface) -> None:
        """ Draw the UI to the screen ."""
        self._manager.draw_ui(screen)
