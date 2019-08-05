def toGoatLatin(S):
    words = S.split() 
    count = 1
    for i in range(0,len(words)):
        if words[i][0] in ['a','e','i','o','u','A','E', 'I','O','U']:
            words[i] = words[i] + 'ma'
        else:
            words[i] = words[i][1:] + words[i][0] + 'ma'
        words[i] = words[i] + 'a' * count
        count+= 1
    return " ".join(words)

S = "I speak Goat Latin"
A = toGoatLatin(S)
print(A)