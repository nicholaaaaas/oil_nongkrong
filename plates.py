import physics_equations


class Plates:
    dist: float
    upper_potential: float
    lower_potential: float

    def __init__(self, dist: float) -> None:
        self.dist = dist
        self.upper_potential = -1
        self.lower_potential = 0

    def set_pd(self, pd) -> None:
        """ Sets the potentials such that the potential difference
            between the plates is <pd> with the electric field pointing
            upwards.
        """
        self.upper_potential = -pd

    def get_pd(self) -> float:
        """
        Returns the potential differences between the upper and the lower plates
        """
        return physics_equations.potential_diff(self.upper_potential,
                                                self.lower_potential)
