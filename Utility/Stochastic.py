from random import random

def weighted_sample(array, weights, k):
    assert len(array) == len(weights)
    temp = [(i, w) for i,w in enumerate(weights)]
    indices = []

    for _ in range(k):
        total_weight = sum(a[1] for a in temp)
        index = -1
        current = 0
        r = random()
        for i, tup in enumerate(temp):
            current += tup[1] / total_weight
            if r < current:
                index = i
                break

        if index == -1:
            index = len(temp) - 1

        indices.append(temp[index][0])
        del temp[index]

    return [array[i] for i in indices]