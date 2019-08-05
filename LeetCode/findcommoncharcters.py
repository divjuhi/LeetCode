def commonChars(A):
    chars = list(set(A[0]))
    v_lsit = [0,0,0]
    dict_count = dict.fromkeys(chars,v_lsit)
    for i in range(len(chars)):
        for j in range(len(A)):
            dict_count[chars[i]][j] = A[j].count(chars[i])
    pass



Input = ["bella","label","roller"]
Output = commonChars(Input)


