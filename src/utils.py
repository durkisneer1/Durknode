import numpy as np


def calculate_bezier_points(
    start: tuple,
    control_1: tuple,
    control_2: tuple,
    end: tuple,
    t: np.ndarray[float],
    inverse_t: np.ndarray[float],
    inverse_t2: np.ndarray[float],
    t2: np.ndarray[float],
) -> list[list]:
    start = np.array(start)
    control_1 = np.array(control_1)
    control_2 = np.array(control_2)
    end = np.array(end)

    points = (
        start * inverse_t2 * inverse_t
        + 3 * control_1 * inverse_t2 * t
        + 3 * control_2 * inverse_t * t2
        + end * t2 * t
    )

    return points.tolist()
