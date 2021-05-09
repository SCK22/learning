import numpy as np
while True:
    low = int(input())
    high = int(input())
    print (low + np.floor((high-low)/2))