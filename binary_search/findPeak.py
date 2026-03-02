nums=[1,2]
def peak(nums):
    low =0
    high=len(nums)-1
    while low<high:#because 
        mid=(low+high)//2
        if nums[mid]>nums[mid+1]:
            high=mid
        else:
            low=mid+1
    return low
    
print(peak(nums))