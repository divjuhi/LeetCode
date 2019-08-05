def convertToTitle(n):
    ref = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    s = ""
    while n > 0:
        n = n-1
        s = ref[n%26]+s
        n = n//26
    return s

n = 26+26+1
s = convertToTitle(n)
print(s)