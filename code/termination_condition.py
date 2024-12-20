def terminate1(individual_list) -> bool:
    BEST_FITNESS = 423.741  # length of the shortest path
    # TODO: in this method, you must check if any individual in the list has reached the 'BEST_FITNESS' value. If yes, return the individual (stop the algorithm), otherwise return None
    target_fitness = -BEST_FITNESS
    for ind in individual_list:
        if ind.fitness is not None and abs(ind.fitness - target_fitness) < 1e-9:
            return ind
    return None