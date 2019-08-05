def flipAndInvertImage(A):
    for i in range(len(A)):
        A[i] = A[i][::-1]
        for j in range(len(A[i])):
            if A[i][j] == 0:
                A[i][j] = 1
            else:
                A[i][j] = 0
    return A 
        

A =[[1,1,1,0],[1,0,1,0],[0,0,0,1]]
print(A)
k = flipAndInvertImage(A)
print(k)



