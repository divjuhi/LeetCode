import numpy as np
import math as mt
def imageSmoother(M):
    row = len(M)
    column = len(M[0])
    new_M= np.empty((row,column), int)
    for i,value1 in enumerate(M):
        for j,value2 in enumerate(value1):
            count = M[i][j]
            number = 1
            for x,y in ((i-1,j),(i+1,j),(i,j-1),(i,j+1),(i-1,j-1),(i-1,j+1),(i+1,j-1),(i+1,j+1)):
                if 0 <= x < row and 0 <= y <column:
                    count += M[x][y]
                    number+=1
            new_M[i][j] = mt.floor(count/number)
    return new_M

M = np.array([[1,1,1],[1,0,1],[1,1,1]])
k = imageSmoother(M)
print(k)






