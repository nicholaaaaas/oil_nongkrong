import physics_equations

class Plates:
    dist: float
    upper_potential: float
    lower_potential: float

    def __init__(self, dist: float, up: float, lp: float) -> None:
        self.dist = dist
        self.upper_potential = up
        self.lower_potential = lp
    
    def get_pd(self) -> float:
        """
        Returns the potential differences between the upper and the lower plates 
        """
        return physics_equations.potential_diff(self.upper_potential, self.lower_potential)