import numpy as np
from scipy import integrate

def scale_scores(y, method="simpson"):
    """
    Scales evenly spaced y values so that integral of graph is one

    :param y: list of y points
    :returns new scaled y points
    """
    score_sum = -1
    if method is "simpson":
        score_sum = integrate.simps(y, dx=1)
    elif method is "trapz":
        score_sum = np.trapz(y, dx=1)

    return map(lambda x: x/score_sum, y)


def scale_all_scores(chars, method="simpson"):
    newDict = {}
    for ch, sc in chars.items():
        new_scores = scale_scores(sc, method=method)
        if not np.isnan(new_scores[0]):
            newDict[ch] = new_scores

    return newDict