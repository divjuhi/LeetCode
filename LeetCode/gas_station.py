def canCompleteCircuit(gas, cost):
    if sum(gas) < sum(cost):
        return -1
    else:
        n = len(gas)
        acc = 0
        start = 0
        minVal = 0
        for i in range(n):
            acc += gas[i] - cost[i]
            if acc < minVal:
                minVal = acc
                start = i + 1
        if acc < 0:
            return -1
        else:
            return start

gas  = [1,2,3,4,5]
cost = [3,4,5,1,2] 
A = canCompleteCircuit(gas, cost)
print(A)
