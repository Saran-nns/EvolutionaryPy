#Cost function or error function (Lower scores)
#Inverse Fiteness function is the measure of optimality of the chromosome

#Fitness value is the total number of correct letters

import chromosome
def fitness(guess):

    return sum(1 for expected,actual in zip(chromosome.target,guess) if expected==actual)


