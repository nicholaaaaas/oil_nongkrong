from __future__ import annotations

from oil import Oil
from plates import Plates
import physics_equations as phy


class Experiment:
    """ A class that represents the Experiment's setup.

        This class is responsible for executing calculations that involve
        both the oil drop and electric plates.
    """

    # === Private Attributes ===
    # _interval: the discrete interval of time used for calculations.
    # _plates: the electric plates in the experiment
    # _oil_drop: the oil drop in the experiment

    _interval: float
    _plates: Plates
    _oil_drop: Oil

    def __init__(self, plates: Plates, oil_drop: Oil) -> None:
        """ Initialize this Experiment to use <plates> and <oil>."""
        self._plates = plates
        self._oil_drop = oil_drop
        self._interval = 1 / 60

    def _get_accel(self, pd: float) -> float:
        """ Calculates the acceleration of the oil_drop. """
        e_strength = phy.electric_field_strength(pd, self._plates.dist)

        e_force = phy.electric_force(e_strength, self._oil_drop.charge)
        g_force = phy.gravitational_force(self._oil_drop.mass)
        net_force = e_force - g_force

        return net_force / self._oil_drop.mass

    def _get_new_vel(self, acc: float, v0: float) -> float:
        """ Return the new velocity of oil_drop given
            an initial velocity <v0> and acceleration <acc>.

            Note: calculations are based on a time interval of length _interval
        """

        return v0 + acc * self._interval

    def _get_new_y(self, acc: float, v0: float, y0: float) -> float:
        """ Return the new (vertical) position of oil_drop given
            initial position <y0>, initial velocity <v0>,
            and acceleration <acc>.

            Note: calculations are based on a time interval of length _interval
        """

        delta_y = v0 * self._interval + 0.5 * acc * (self._interval ** 2)
        return y0 + delta_y

    def update(self, time_delta: float) -> None:
        """ Update the state of this experiment. In particular,
            recompute the position and velocity of the oil drop.

            Note: Notice that pygame coordinates increase going
                down while physical values decrease going down.
                This function handles all necessary translations.
        """
        self._interval = time_delta  # time passed since the last frame
        pd = self._plates.get_pd()
        actual_acc = self._get_accel(pd)
        new_acc = -actual_acc  # need to reverse for pygame coordinates
        self._oil_drop.position = self._get_new_y(new_acc,
                                                  self._oil_drop.velocity * 6.5,
                                                  self._oil_drop.position)
        self._oil_drop.velocity = self._get_new_vel(new_acc,
                                                    self._oil_drop.velocity)
        

    def get_plates(self) -> Plates:
        """ Return this experiment's plates. """
        return self._plates

    def get_oil_drop(self) -> Oil:
        """ Return this experiment's oil drop. """
        return self._oil_drop
