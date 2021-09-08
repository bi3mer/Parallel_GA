from bisect import bisect_left

def insert(solutions, scores, sol, fit, max_length):
    # if max length then either the score should be added to the solutions and
    # scores and we remove the lowest values, or the score is low enough that 
    # it should not be added.
    if len(solutions) >= max_length:
        if fit < scores[-1]:
            solutions.pop()
            scores.pop()
        else:
            return

    insert_index = bisect_left(scores, fit)
    solutions.insert(insert_index, sol)
    scores.insert(insert_index, fit)

def binary_search(solutions, fitness):
    low = 0
    high = len(solutions) - 1
    mid = 0

    while low <= high:
        mid = (low + high) // 2
        if solutions[mid][0] < fitness:
            low = mid + 1
        elif solutions[mid][0] > fitness:
            high = mid - 1
        else:
            return mid

    return low

def insert_tup(solutions, new_solution, fitness, max_length, minimize=True):
    # solutions => p(score, solution), ...]
    if len(solutions) >= max_length:
        if minimize:
            if fitness < solutions[-1][0]:
                solutions.pop()
            else:
                return
        else:
            if fitness > solutions[-1][0]:
                solutions.pop()
            else:
                return
    
    solutions.insert(binary_search(solutions, fitness), (fitness, new_solution))
