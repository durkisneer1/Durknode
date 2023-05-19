import numpy as np

t = np.linspace(0, 1)
t = t[:, np.newaxis]
inverse_t = 1 - t
inverse_t2 = inverse_t**2
t2 = t**2


def calculate_bezier_points(pos1: np.array, pos2: np.array):
    vertical_distance = np.abs(pos2[1] - pos1[1])
    offset = vertical_distance * 0.5

    control_1 = pos1 + (offset, 0)
    control_2 = pos2 - (offset, 0)

    points = (
        pos1 * inverse_t2 * inverse_t
        + 3 * control_1 * inverse_t2 * t
        + 3 * control_2 * inverse_t * t2
        + pos2 * t2 * t
    )
    return points
