
def search(nums,target):
    def binS(nums,target,low,high):
        while low<=high:
            mid=(low+high)//2
            if nums[mid]==target:
                return mid
            elif target<nums[mid]:
                high=mid-1
            else:
                low=mid+1
        return -1
    idx=0
    if len(nums)==1 and target==nums[0]:
        return 0
    elif len(nums)==1:
        return -1
    if nums[0]>nums[-1]:
        for i in range(len(nums)-1):
            if nums[i]>nums[i+1]:
                idx=i
        
            
        if target<nums[0]:
            return binS(nums,target,idx+1,len(nums)-1)
        else:
            
            return binS(nums,target,0,idx)
    else:
        
        return binS(nums,target,0,len(nums)-1)
        

nums = [3,5,1]
target = 3
print(search(nums,target))




        