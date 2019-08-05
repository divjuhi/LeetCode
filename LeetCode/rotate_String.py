def rotateString(A, B):
    if len(A)!= len(B) or A != ''.join(sorted(B)):
        return False
    else:
        c= B.find(A[0])
        B = B[c:] + B[0:c]
        if A != B:
            return False
        else:
            return True


A = 'abcde'
B = 'cdeab'
C = rotateString(A, B)
print(C)
