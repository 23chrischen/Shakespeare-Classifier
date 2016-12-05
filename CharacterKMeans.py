import math
import random
import numpy as np
from scipy import integrate


# c1,c2 are lists of values w/ same length
def character_distance(c1, c2, method="simpson", squared=True):
    if len(c1) != len(c2):
        print len(c1)
        print len(c2)
        raise ValueError("Characters arrays not same length!")

    abs_diff = []

    for i in range(len(c1)):
        abs_diff.append(abs(c1[i] - c2[i]))

    if method is "simpson":
        dist = integrate.simps(abs_diff, dx=1)
    elif method is "trapz":
        dist = np.trapz(abs_diff, dx=1)
    else:
        raise ValueError("Invalid method param given")
    if squared:
        dist = dist**(2)

    return dist

# chars is dict of characters, centers is list of k centers
# returns array of length k, k is kth center and array element
# array of character names (strings) closest to that center
def char_clusters(chars, centers):
    res = [[] for i in range(len(centers))]
    for charName, charPoints in chars.items():
        shortestDist = character_distance(charPoints, centers[0])
        closestCenter = 0
        for i in range(1, len(centers)):
            d = character_distance(centers[i], charPoints)
            if d < shortestDist:
                shortestDist = d
                closestCenter = i
        res[closestCenter].append(charName)
    return res


def calculate_centers(chars, clusters):
    centers = []
    for cl in clusters:
        cent = [chars[name] for name in cl] # a list of lists of points of characters in cl
        cent = [sum(x) for x in zip(*cent)]
        cent = map(lambda m: float(m)/len(cl), cent)
        centers.append(cent)
    return centers


# chars is dict with only numbers in columns i.e. distance function
# is square root of sum of squares of columns
# returns: list of k tuples representing clusters which hold (centerlist, charnames)
def characterKMeans(chars, k, max_iter=100):
    cent_keys = np.random.choice(chars.keys(), size=k, replace=False)
    centers = []
    for key in cent_keys:
        centers.append(chars[key])

    for it in range(max_iter):
        clusters = char_clusters(chars, centers)
        centers = calculate_centers(chars, clusters)
    final_clusters = char_clusters(chars, centers)
    final_centers = calculate_centers(chars, final_clusters)
    return zip(final_centers, final_clusters)


def merge_two_dicts(x, y):
    '''Given two dicts, merge them into a new dict as a shallow copy.'''
    z = x.copy()
    z.update(y)
    return z


def predictCluster(chars, centers, charDict):
    merged = merge_two_dicts(chars, charDict)
    return char_clusters(merged, centers)


