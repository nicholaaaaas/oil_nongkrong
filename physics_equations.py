def electric_field_strength(p_diff: float, dist: float) -> float:
    """ Return the strength of the electric field given
        potential difference <p_diff> and distance <dist> between plates.
    """
    pass


def electric_force(e_strength: float, charge: float) -> float:
    """ Return the magnitude of the electric force acting on a <charge>-charged
        object under an electric field of strength <e_strength>.
    """
    pass


def gravitational_force(m: float) -> float:
    """ Return the gravitation force acting on an object of mass <m>.
    """
    pass


def potential_diff(p1: float, p2: float) -> float:
    """ Return the potential difference between <p1> and <p2>.

        Note: the potential difference returned will always be non-negative.
    """
    return abs(p1 - p2)
