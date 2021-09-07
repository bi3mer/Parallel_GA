def distance(a, b):
    return sum([(a_i - b_i)**2 for a_i, b_i in zip(a, b)]) ** 0.5

def distance_squared(a, b):
    return sum([(a_i - b_i)**2 for a_i, b_i in zip(a, b)])