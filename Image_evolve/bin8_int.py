#This function converts a string of 8 binary digits to an integer
import numpy as np
def bin8_to_int(b8):
    #print (np.shape(b8))
    #b8=np.asarray(b8)
    #print (b8)
    length = len(b8)
    #print(length)
    num = 0
    for i in range(length):
        num = num + b8[i]
        num = num * 2
    return num // 2


x1=[0,1,1,1,1,1,1,1]
x2=[1,1,1,1,1,1,1,0]
xx=bin8_to_int(x1)
xxx=bin8_to_int(x2)
print (xx,xxx)
#print(bin8_to_int(b8))
    
