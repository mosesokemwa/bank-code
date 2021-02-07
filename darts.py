"""A simple darts game.

The program asks the user to provide two inputs x and y. These points
represent the location (x, y) on a 2-dimensional dart target (a circle).

The program returns the correct amount earned by a dart landing at that point.
"""

OUTER_CIRCLE_RADIUS = 10
MIDDLE_CIRCLE_RADIUS = 5
INNER_CIRCLE_RADIUS = 1
CENTRE = (0, 0)


def score(x: float, y: float):
    """Returns the points earned given location (x, y) by
    finding the distance to the centre defined at (0, 0).

    Parameters
    ----------
    x : float,
        The cartesian x-coordinate on the target
    y : float,
        The cartesian y-coordinate on the target
    """
    try:
        x = abs(float(x))
        y = abs(float(y))
    except ValueError:
        print('ValueError: The functionn score only accepts floats as inputs')
        return

    distance_to_centre = ( (x - CENTRE[0])**2 + (y - CENTRE[1])**2 ) ** (0.5)

    if distance_to_centre > OUTER_CIRCLE_RADIUS:
        return 0
    elif MIDDLE_CIRCLE_RADIUS < distance_to_centre <= OUTER_CIRCLE_RADIUS:
        return 1
    elif INNER_CIRCLE_RADIUS < distance_to_centre <= MIDDLE_CIRCLE_RADIUS:
        return 10
    elif 0 <= distance_to_centre <= INNER_CIRCLE_RADIUS:
        return 5


if __name__ == '__main__':
    x, y = input('Provide the cartesian coordinates x and y: ').split()
    s = score(x, y)
    print(f'Points earned: {s}')