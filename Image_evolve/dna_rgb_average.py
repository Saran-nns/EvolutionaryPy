#This function computes the RGB image by averaging the R, G, and B values from each block.

import random
import numpy as np
import bin8_int
import numbapro as numba
from numbapro import vectorize


#@vectorize (['float32(float32)'],target='gpu')
@numba.jit(nopython=False)
def dna_to_rgb_average(*dna):
    """Parameters:

        Input: integer DNA(56,32), the 8 bits of the 7 "genes" of the 32 "chromosomes" of the DNA.

        Output: uint8 RGB(3,256,256), the RGB information."""
    chromosome = np.zeros (( 256, 256 ),dtype='float32')
    rgb = np.zeros ((256, 256,3),dtype='float32')
    dna=np.asarray(dna,dtype='float32')   #Because the *arg is always a tuple, regardless of what is provided
    for j in range (len(dna[0])):
        
        x1 = bin8_int.bin8_to_int(dna[0:8,j])
        y1 = bin8_int.bin8_to_int(dna[9:16,j])
        x2 = bin8_int.bin8_to_int(dna[17:24,j])
        y2 = bin8_int.bin8_to_int(dna[25:32,j])
        r = bin8_int.bin8_to_int(dna[33:40,j])
        g = bin8_int.bin8_to_int(dna[41:48,j])
        b = bin8_int.bin8_to_int(dna[49:56,j])
        
        #Get the lowest and highest values from x and y and use them as the width and height of the rectangle
        
        xlo = min ( x1, x2 )+1     
        xhi = max ( x1, x2 )+1
        ylo = min ( y1, y2 )+1
        yhi = max ( y1, y2 )+1

        chromosome[xlo:xhi,ylo:yhi]=chromosome[xlo:xhi,ylo:yhi]

        rgb[xlo:xhi,ylo:yhi,0] = rgb[xlo:xhi,ylo:yhi,0]  + r
        rgb[xlo:xhi,ylo:yhi,1] = rgb[xlo:xhi,ylo:yhi,1]  + g
        rgb[xlo:xhi,ylo:yhi,2] = rgb[xlo:xhi,ylo:yhi,2]  + b

     
    rgb[0:255,0:255,0] =rgb[0:255,0:255,0] / chromosome[0:255,0:255]
    rgb[0:255,0:255,1] =rgb[0:255,0:255,1] / chromosome[0:255,0:255]
    rgb[0:255,0:255,2] =rgb[0:255,0:255,2] / chromosome[0:255,0:255]
    rgb = np.uint8 ( rgb )

    return rgb
"""
q=np.random.random((56,32))
print (np.shape(q))
print (dna_to_rgb_average(q))
print (np.shape(dna_to_rgb_average(q)))"""
