#Chromosome is a string: Represents a solution candidate

import random

#Function to generate parent chromosome
#Geneset#Genotypes
geneSet="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!(){}; "
target="while(noSuccess){ tryAgain(); if(Dead) break}"

def genotype(length):
    genes=[]
    while len(genes)<length:
        sampleSize=min(length-len(genes),len(geneSet))
        genes.extend(random.sample(geneSet,sampleSize))
    return ''.join(genes)







