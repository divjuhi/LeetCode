import numpy as np

def separate_Odd_Even(Array):
    Even = []
    Odd =[]
    for x in Array:
        if x%2 == 0:
            Even = np.concatenate((Even,[x]), axis = 0, out= None)
        else:
            Odd = np.concatenate((Odd,[x]), axis=0, out= None)
    Result = np.concatenate((Odd,Even), axis=0, out= None)
    print(Result)

arr = [5, 7, 8, 9, 10, 34, 56, 1, 2, 7]
separate_Odd_Even(arr)

