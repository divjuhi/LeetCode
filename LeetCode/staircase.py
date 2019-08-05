def arrangeCoins(n):
	k = 0
	i = 1
	while n >= i:
		print('.' *  i)
		print()
		n = n-i
		i +=1
	return i-1

n = 2
k = arrangeCoins(n)
print(k)