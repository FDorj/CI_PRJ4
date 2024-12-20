from individual import Individual
import random

def cross_over(parent1: Individual, parent2: Individual):
    # TOOD
    # We'll implement Order Crossover (OX).
    size = len(parent1)
    child1 = [None] * size
    child2 = [None] * size

    # Select two crossover points
    start, end = sorted(random.sample(range(size), 2))

    # Copy the segment from parent1 to child1
    child1[start:end+1] = parent1.genome[start:end+1]

    # Fill the rest of child1 from parent2 in order
    p2_items = [g for g in parent2.genome if g not in child1]
    idx = 0
    for i in range(size):
        if child1[i] is None:
            child1[i] = p2_items[idx]
            idx += 1

    # Do the same for child2
    child2[start:end+1] = parent2.genome[start:end+1]
    p1_items = [g for g in parent1.genome if g not in child2]
    idx = 0
    for i in range(size):
        if child2[i] is None:
            child2[i] = p1_items[idx]
            idx += 1

    offspring1 = Individual(generate_random_genome=False)
    offspring1.genome = child1
    offspring2 = Individual(generate_random_genome=False)
    offspring2.genome = child2

    return offspring1, offspring2