import random
import numpy as np
import bin8_int
import numbapro as numba
from numbapro import vectorize

@numba.jit(nopython=False)
#@vectorize(['float32(float32)','float64(float64,float64)'],target='gpu')

def dna_to_rgb_max(*dna):
    """
    DNA_TO_RGB_MAX creates an RGB image from DNA
    
    Input, integer DNA(56,32), the 8 bits of the 7 "genes" of the  32 "chromosomes" of the DNA.
    Output, uint8 RGB(3,256,256), the RGB information.
    """
    chromosome = np.zeros (( 256, 256 ),dtype='uint8')
    rgb = np.zeros ((256, 256,3),dtype='uint8')
    dna=np.asarray(dna)
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

        nx=xhi-xlo
        ny=yhi-ylo

        rmat=r*np.ones((nx,ny),dtype="uint8")
        gmat=g*np.ones((nx,ny),dtype="uint8")
        bmat=b*np.ones((nx,ny),dtype="uint8")

        chromosome[xlo:xhi,ylo:yhi]=chromosome[xlo:xhi,ylo:yhi]

        rgb[xlo:xhi,ylo:yhi,0] = rgb[xlo:xhi,ylo:yhi,0] + r
        rgb[xlo:xhi,ylo:yhi,1] = rgb[xlo:xhi,ylo:yhi,1] + g
        rgb[xlo:xhi,ylo:yhi,2] = rgb[xlo:xhi,ylo:yhi,2] + b

    #print (np.shape(rgb))
    rgb[xlo:xhi,ylo:yhi,0] =np.maximum(rgb[xlo:xhi,ylo:yhi,0].astype(int), rmat[0:nx,0:ny].astype(int))
    rgb[xlo:xhi,ylo:yhi,1] =np.maximum(rgb[xlo:xhi,ylo:yhi,1].astype(int), gmat[0:nx,0:ny].astype(int))
    rgb[xlo:xhi,ylo:yhi,2] =np.maximum(rgb[xlo:xhi,ylo:yhi,2].astype(int), bmat[0:nx,0:ny].astype(int))
    rgb = np.uint8 ( rgb )

    return rgb
"""
q=np.random.random((56,32))
print (dna_to_rgb_max(*q))
print (np.shape(dna_to_rgb_max(*q)))"""

