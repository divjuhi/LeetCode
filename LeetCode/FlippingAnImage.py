import numpy as np
def flipAndInvertImage(A):
    row = A.shape[0]
    column = A.shape[1]
    B = np.empty((row,column))
    for i,value in enumerate(A):
        B[i,:] = value[::-1]
        for j,value in enumerate(B[i]):
            if value == 0:
                B[i][j] = 1
            else:
                B[i][j] = 0
    return B

        

A = np.array([[1,1,0],[1,0,1],[0,0,0]])
k = flipAndInvertImage(A)
print(A)
print(k)



