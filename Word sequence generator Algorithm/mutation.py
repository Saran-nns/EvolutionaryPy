#Crossover may get us stuck near the local optimum
"""To produce new guess, mutate current guess."""

import chromosome
import cost_function
import random

def mutate(parent):
    childGenes=list(parent) #Covert parent string to an array
    #Replace one letter in the array with randomly generated one
    index=random.randint(0,len(parent)-1)
    newGene,alternate=random.sample(chromosome.geneSet,2)
    childGenes[index]=alternate\
                       if newGene==childGenes[index]\
                       else newGene
    #Recombine the result into a string
    return ''.join(childGenes)
    
"""
parent= chromosome.genotype(12)
print (parent)
print (cost_function.fitness(chromosome.genotype(12)))
print (mutation(parent))
"""

