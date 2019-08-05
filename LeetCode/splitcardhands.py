def isNStraightHand(hand, W):
 
    n = len(hand)
    if n%W != 0: return False
    hand.sort()
    while hand:
        cur = hand[0]
        for i in range(W):
            if cur in hand:
                hand.remove(cur)
            else:
                return False
            cur += 1
    return True

hand =[1,2,3,6,2,3,4,7,8]
W = 3
A = isNStraightHand(hand, W)
print(A)