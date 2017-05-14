
import random
import datetime
import chromosome
import cost_function
import mutation

#Visual representation of the gene sequence,fitness value and total runtime
def display(guess):
    
    timeDiff=datetime.datetime.now()- startTime
    fitness=cost_function.fitness(guess)
    print("{0}\t{1}\t{2}".format(guess,fitness,str(timeDiff)))

random.seed()
startTime=datetime.datetime.now()
bestParent=chromosome.genotype(len(chromosome.target))
bestFitness=cost_function.fitness(bestParent)
display(bestParent)

#Build Guess loop

while True:
    child=mutation.mutate(bestParent)
    childFitness=cost_function.fitness(child)
    if bestFitness >=childFitness:
        continue
    display(child)
    if childFitness >=len(bestParent):
        break
    bestFitness,bestParent=childFitness,child


def main():
    if __name__=="__main__":
        main()

print("--%s seconds--"%(datetime.datetime.now()-startTime))
