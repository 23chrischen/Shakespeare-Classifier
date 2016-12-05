import numpy as np

def interpolate_points(function_points, interp_x):
    """
    Linearly interpolates y values between points for given x values

    :param function_points: list of points which define the function whose range is [a,b]
    :param interp_x: list of x points for which you want to get interpolated values
    :returns list of (x, y) points for interp_x values
    """

    result = []
    fcn_sorted = sorted(function_points, key=lambda point: point[0])
    xp, yp = zip(*fcn_sorted)
    return zip(interp_x, np.interp(interp_x, xp, yp))

# Pass number of points for each character to have
def interpolate_chars_uniformly(char_score_dict, num_points=200):
    new_dict = {}
    for ch, sc in char_score_dict.items():
        interp_points = [float(x)/num_points for x in range(num_points)]
        new_dict[ch] = interpolate_points(sc, interp_points)
    return new_dict

def test():
    points = [(0,0), (2,0), (4,2), (6, -2)]
    interps = [0, 1, 3, 5]
    expected_y = [0, 0, 1, 0]

    x2, y2 = zip(*interpolate_points(points, interps))

    print "The two following arrays should be equal:\n" + str(expected_y) + \
          "\n" + str(y2)