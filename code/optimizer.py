import random

from individual import Individual
from evaluation import evaluate_all, evaluate
import evaluation
from selection import select_two_individual_for_crossover

from crossover import cross_over
from mutation import mutation1
from termination_condition import terminate1


def run_algorithm(
    distance_matrix,
    population_size=20,
    generation_size=30,
):
    # Set the global distance matrix for evaluation
    evaluation.distance_matrix = distance_matrix
    
    MUTATION_RATE = 0.3
    best_fitness_list = []
    avg_fitness_list = []
    best_individual = None
    genome_size = len(distance_matrix)

    # create primary population
    population = primary_population_creator(population_size, genome_size)
    evaluate_all(population)

    while True:
        # cross over
        generated_individuals = []
        for _ in range(int(generation_size / 2)):
            # TODO
            parent1, parent2 = select_two_individual_for_crossover(population, population_size)
            offspring1, offspring2 = cross_over(parent1, parent2)
            generated_individuals.append(offspring1)
            generated_individuals.append(offspring2)

        # mutation
        for individual in generated_individuals:
            # TODO: by using a random number and 'MUTATION_RATE', decide whether to mutate the individual or not    
            if random.random() < MUTATION_RATE:
                mutation1(individual)

        # TODO: evaluate generated_individuals
        evaluate_all(generated_individuals)

        # TODO: select next generation by use of 'next_generation_selection' method
        population = next_generation_selection(population, generated_individuals, population_size)

        # TODO: check termination condition on generated individuals
        terminating_individual = terminate1(population)
        if terminating_individual is not None:
            best_individual = terminating_individual
            break

        # TODO: redefine 'population' for the next iteration
        

        # don't change following codes
        best_fitness_list.append(best_fitness(population))
        avg_fitness_list.append(avg_fitness(population))
        random.shuffle(population)

    return best_individual, best_fitness_list, avg_fitness_list

def primary_population_creator(
    population_size: int, genome_size: int
) -> list[Individual]:
    # TODO: this method create primary individual based on input population size and return them as list of individuals
    population = [Individual(genome_length=genome_size, generate_random_genome=True) for _ in range(population_size)]
    return population

def avg_fitness(
        population:list[Individual]
) -> float:
    # TODO: this method calculates average of individuals fitness
    total = sum(ind.fitness for ind in population if ind.fitness is not None)
    return total / len(population)


def best_fitness(
        population:list[Individual]
) -> float:
    # TODO: this method finds best fitness in the population
    return max(ind.fitness for ind in population if ind.fitness is not None)

def next_generation_selection(old_population, new_individuals, population_size):
    # Combine old and new
    combined = old_population + new_individuals
    # Sort by fitness (descending, since we want max fitness)
    combined.sort(key=lambda x: x.fitness, reverse=True)
    # Take top population_size
    return combined[:population_size]