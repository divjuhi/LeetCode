def repeatedSubstringPattern(self):
	rep_string = input[0]
	for i in range(1,len(self)):
		if input[i:i+len(rep_string)] == rep_string:
			print('true')
			rep_string = rep_string + input[i:i+len(rep_string)]
			i+= 1
		else:
			rep_string = rep_string + input[i]

input = "abab"
r = repeatedSubstringPattern(input)
print(r)