nums = [1,2,5,9]
import math
threshold = 6
def samllestDivisor(nums,thershold):
    def check(nums,divisor,threshold):
                res=0
                for n in nums:
                    res+=math.ceil(n/divisor)
                return res<=threshold
    l=1
    r=max(nums)

    while l<=r:
        mid=(l+r)//2
        if  check(nums,mid,threshold):
            r=mid-1
        else:
            l=mid+1
    return l


        