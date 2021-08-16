from math import sqrt

def distance(a, b):
    return sqrt(sum([(a_i - b_i)**2 for a_i, b_i in zip(a, b)]))

def distance_squared(a, b):
    return sum([(a_i - b_i)**2 for a_i, b_i in zip(a, b)])