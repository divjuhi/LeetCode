import numpy as np

def separate_Odd_Even(Array):
    for i in range(0,len(Array)):
        if Array[i]%2!=0:
            break
        else:
            for j in range(i-1,-1,-1):
            if Array[j]%2 != 0:
                

arr = [5, 6, 7, 8, 9, 10, 34, 56, 1, 2, 7]
separate_Odd_Even(arr)

