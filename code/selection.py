from individual import Individual
import random

def select_two_individual_for_crossover(
    individual_list: list[Individual], population_size: int
) -> tuple[Individual, Individual]: # you can change return type based on your implementation
    # TODO: this method selects two individuals for the crossover algorithm
    parent1 = random.choice(individual_list)
    parent2 = random.choice(individual_list)
    while parent2 == parent1:
        parent2 = random.choice(individual_list)
    return parent1, parent2