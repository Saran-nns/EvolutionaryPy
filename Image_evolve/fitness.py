import numpy as np
def rgb_fitness (m, n,k, in_image, b ):
    """
    RGB_FITNESS scores image B as a match for in_image .
    
    Parameters:

    Input, integer M, N, K, the dimensions of the images.

    Input, uint8 in_image(M,N,K), the original image.

    Input, uint8 B(M,N,K), the approximate image.

    Output, int SCORE, a score for the matching."""
    score= np.sum( np.sum ( np.sum ( abs ( np.float32 ( in_image ) - np.float32 ( b ) ) ) ) )
    return score
"""
image=[[[np.random.random() for m in range(256)] for n in range(256)] for k in range(3)]
print image"""
