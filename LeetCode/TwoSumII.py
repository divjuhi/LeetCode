
def twoSum(numbers, target):
    start = 0
    end = len(numbers)-1
    while(start<end and numbers[start]+numbers[end]!= target):
        if numbers[start]+numbers[end] > target:
            end -= 1
        else:
            start+= 1
    return start,end

numbers = [2,7,11,15,18,20,30]
target = 9
A = twoSum(numbers, target)
print(A)