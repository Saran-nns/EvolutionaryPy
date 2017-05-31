import numpy as np
import random
import os
from scipy.ndimage import imread
img=os.path.join('C:/Users/Saran/!Imgevolve/image.png')
in_image=np.uint8(imread(img,flatten=False,mode='RGB'))
#in_image=np.uint8(in_image)
print (np.shape(in_image))

