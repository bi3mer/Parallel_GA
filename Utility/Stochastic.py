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


def weighted_sample_tup(array,  k, reverse=False):
    # [(fitness, strand), ...] => array
    if reverse:
        worst_fitness = max(array, key=lambda x: x[0])[0]
        temp_array = [(worst_fitness - ele[0], ele[1]) for ele in array]

        return weighted_sample_tup(temp_array, k)

    valid_indices = list(range(len(array)))
    indices = []

    for _ in range(k):
        # total_weight = sum(array[i][0] for i in valid_indices)
        current = 0
        r = random()
        for index_index, array_index in enumerate(valid_indices):
            current += array[array_index][0]
            if r < current:
                break

        indices.append(array_index)
        del valid_indices[index_index]

    return [array[i] for i in indices]