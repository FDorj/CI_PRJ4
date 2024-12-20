from individual import Individual
import random

def mutation1(individual: Individual):
    # TODO: this method applies mutation on an individual
    size = len(individual)
    i, j = random.sample(range(size), 2)
    individual.genome[i], individual.genome[j] = individual.genome[j], individual.genome[i]
