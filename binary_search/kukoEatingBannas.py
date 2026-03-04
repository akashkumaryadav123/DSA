import math
piles = [3,6,7,11]

h = 8
def canEatAll(piles,h,k):
    hoursUsed=0
    for p in piles:
        hoursUsed+=math.ceil(float(p)/k)
    return hoursUsed <=h
def cocoEat (piles,h):
    left,right=1,max(piles)
    
    
    while left<=right:
        mid=(left+right)//2
        if canEatAll(piles,h,mid):
            
            right=mid-1
        else:
            left=mid+1
    return left
print(cocoEat(piles,h))