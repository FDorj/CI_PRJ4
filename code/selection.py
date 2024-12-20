from individual import Individual
import random

def select_two_individual_for_crossover(
    individual_list: list[Individual], population_size: int
) -> tuple[Individual, Individual]: # you can change return type based on your implementation
    # TODO: this method selects two individuals for the crossover algorithm
    def tournament(k=3):
        aspirants = random.sample(individual_list, k)
        aspirants.sort(key=lambda x: x.fitness, reverse=True)
        return aspirants[0]

    parent1 = tournament()
    parent2 = tournament()
    while parent2 == parent1:
        parent2 = tournament()
    return parent1, parent2