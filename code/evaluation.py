from individual import Individual

# We'll have a global variable distance_matrix set from outside or pass it as parameter.
# For simplicity, let's store it globally or assume it's set externally.
distance_matrix = None

def evaluate_all(individual_list: list[Individual]):
    for individual in individual_list:
        evaluate(individual)


def evaluate(individual: Individual):
    # TODO: this method computes fitness (based on the TSP problem) and updates the fitness attribute of the individual parameter (individual.fitness=new_fitness)
    # hint: as taught by Dr. Ebadzadeh in the class, you may use -c to reverse the fitness value c
    total_distance = 0.0
    for i in range(len(individual)-1):
        total_distance += distance_matrix[individual.genome[i]][individual.genome[i+1]]
    # Add return to start if needed
    total_distance += distance_matrix[individual.genome[-1]][individual.genome[0]]

    individual.fitness = -total_distance
