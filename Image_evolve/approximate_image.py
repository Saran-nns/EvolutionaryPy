
import os
from scipy.ndimage import imread
import matplotlib.pyplot as plt
from PIL import Image
import numpy as np
import math
import i4mat_write
import dna_rgb_average
import dna_rgb_max
import fitness
from numbapro import vectorize
import random
import itertools
import numbapro as numba


img=os.path.join('C:/Users/Saran/!Imgevolve/image.png')
in_image=np.uint8(imread(img,flatten=False,mode='RGB'))
#in_image=np.uint8(in_image)
print (np.shape(in_image))

@numba.jit(nopython=False)
#@vectorize (['float32(float32)','float64(float64)'],target='gpu')
def image_match(img):
    
    #Approximates an image with 32 colored rectangle"""

    """
    Parameters:
    Input, string img (filename)
    """
    plt.imshow(in_image)
    plt.title('Image to match')
    
    [m,n,k]=np.shape(img)
    
    #Generate an initial population of 10 candidates.
    
    dna_num = 10; 
    """10,(7*8),32 mean that number of candidate solutions(DNAs) are 10 and for each DNA, we have 32 colored 
    rectangle(chromosomes) which itself represented by 7 genes(4 coordinates(bottom-left and top-right)+ R,G,B values)
    using 8 bits for each gene member since each gene member is an integer between 0 and 255"""
    
    dna_pool=[0]*dna_num  # Initialize the dna lists: Shape should be (10,56,32)
    #dna_pool=np.uint8(dna_pool)
    #gene_pool=np.zeros((56,32,dna_num)) 

    for idx,dna in enumerate(dna_pool):
        dna=np.ones((56,32),dtype='uint8')
        for x in range(0,len(dna[1])): #56
            for y in range(0,len(dna[0])): #32
                dna[x][y]= random.choice([0,1]);
        dna_pool[idx]=dna
    
    """
    print (np.shape(dna_pool))
    print (dna_pool[9])
    print (dna_pool[9][0:8,0])
    print (len(dna_pool[9][0]))
    print (np.shape(dna_pool[0]))
    """
    #Evolution Loop begins
    
    score_sofar=math.inf
    score_idx=0
    step_max = 10000

    while True:
        #Create the RGB array corresponding to each set of DNA, determine the scores.
        score = [0]*dna_num
        for i in range(len(dna_pool)-1):
            rgb = dna_rgb_average.dna_to_rgb_average(*dna)
            rgb = dna_rgb_max.dna_to_rgb_max(*dna) 
            score[i] = fitness.rgb_fitness (256,256,k, in_image, rgb )

        score_min = math.inf
        score_index = 0
        step=0
        for j in range (len(dna_pool)):
            if ( score[j] < score_min ):
                score_min = score[j]
                score_index = j
                step+=1
 
        if ( score_min < score_sofar ):
            print(" step , score_index , score_min ", step, score_index, score_min )
            score_sofar = score_min
                    
    #Reorder the DNA so lowest (best) scores are first.

        for j in range(dna_num-1):
            for k in range( j + 1, dna_num):
                if ( score[k] < score[j] ):
                    t= score[k]
                    score[k] = score[j]
                    score[j] = t
                    t = dna_pool[k]
                    dna_pool[k] = dna_pool[j]
                    dna_pool[j] = t

        if step==0:
            filename='best.txt'
            i4mat_write.i4mat_write(filename,56,32,dna_pool[0])
            rgb=dna_rgb_average.dna_to_rgb_average(dna_pool[0])
            rgb=dna_rgb_max.dna_to_rgb_max(dna_pool[0])
            plt.imshow(rgb)

image_match(in_image)
        
        

                    

        
        
    
    
    






    
   
