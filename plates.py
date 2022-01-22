import physics_equations
from typing import Tuple


class Plates:
    dist: float
    upper_potential: float
    lower_potential: float
    pd_range: Tuple[float, float]

    def __init__(self, dist: float, pd_range: Tuple[float, float] = (0, 250)) -> None:
        self.dist = dist
        self.upper_potential = -1
        self.lower_potential = 0
        self.pd_range = pd_range

    def set_pd(self, pd) -> None:
        """ Sets the potentials such that the potential difference
            between the plates is <pd> with the electric field pointing
            upwards.

            Note: the range of accepted values is determined by the pd_range
                specified during initialization.
        """
        if pd >= self.pd_range[0] and pd <= self.pd_range[1]:
            self.upper_potential = -pd

    def get_pd(self) -> float:
        """ Returns the potential differences between the upper and the lower plates.
        """
        return physics_equations.potential_diff(self.upper_potential,
                                                self.lower_potential)
