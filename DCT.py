import cv2
import numpy as np
from numpy import random
import math
sum = 0
arr = np.random.randint(0, 255, size=(8, 8))
print('array :\n')
print(arr)
dct = np.zeros((8,8))
val = 0
for i in range(0,7):
    for j in range(0,7):
        if i == 0 :
            ci = 1/math.sqrt(2)
        else :
            ci = 1/2
        if j == 0 :
            cj = 1/math.sqrt(2)
        else :
            cj = 1/2
        sum = 0
        for k in range(0,7):
            for m in range(0,7):
                val = math.cos((2*k + 1)*i*math.pi / (16)) * math.cos((2*m + 1)* j*math.pi /(16))
                sum += val
        
        dct[i][j] = sum*ci*cj
print('\ndct is :\n')
print(dct)