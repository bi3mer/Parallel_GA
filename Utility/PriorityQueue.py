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
