import random


class Solution(object):
	
	def __init__(self, nums):
		self.array = nums
		self.original = list(nums)

	def shuffle(self):
		random.shuffle(self.array)
		aux = self.array
		return aux
	
	def reset(self):
		aux = self.original
		return aux
	
	def shuffle_algo(self):
		for i in range(len(self.array)):
			swap_idx = random.randrange(i, len(self.array))
			self.array[i], self.array[swap_idx] = self.array[swap_idx], self.array[i]
		return self.array
		



nums = [1,2,3,4,5,6]
obj = Solution(nums)
#param_1= obj.reset()
#param_2 = obj.shuffle()
param_3 = obj.shuffle_algo()

#print(param_1)
print(param_3)

