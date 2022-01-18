from scipy import constants


def electric_field_strength(p_diff: float, dist: float) -> float:
    """ Return the strength of the electric field given
        potential difference <p_diff> and distance <dist> between plates.

        Note: electric field strength is a vector. Therefore, we can say that
        it assumes a negative value when electric field is pointing downwards,
        and vice versa
    """
    return p_diff / dist


def electric_force(e_strength: float, charge: float) -> float:
    """ Return the magnitude and direction of the electric force acting on
        a <charge>-charged object under an electric field of strength
        <e_strength>.
    """
    return e_strength * charge


def gravitational_force(m: float) -> float:
    """ Return the gravitation force acting on an object of mass <m>.
    """
    return m * constants.g


def potential_diff(p1: float, p2: float) -> float:
    """ Return the potential difference between <p1> and <p2>, where <p1> is
        the potential in the upper plate, and <p2> is the potential in the
        lower plate.

        Note: the potential difference is positive if electric field is
        pointing upwards (where potential in upper plate is negative, and
        potential in lower plate is positive); potential difference is negative
        if electric field is pointing downwards (where potential in upper plate
        is positive, and lower plate is negative)
    """
    return p2 - p1


def charge_oil(m: float, acc: float, dist: float, p_diff: float) -> float:
    return (m * (acc + constants.g) * dist) / p_diff


def acceleration(m: float, grav_force: float, elec_force: float) -> float:
    """ Returns the acceleration of the charged oil.

        Note: a negative acceleration indicates that the oil is going in the
        direction of the gravitational force, and a positive acceleration
        indicates that the oil is going in the direction of electric force.
    """
    return (grav_force - elec_force) / m


def velocity(acc: float, time: float) -> float:
    """ Return the velocity of the charged oil

        Note: a negative velocity indicates that the oil is going in the
        direction of the gravitational force, and a positive velocity indicates
        that the oil is going in the direction of electric force.
    """
    return acc * time
