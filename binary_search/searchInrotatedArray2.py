nums = [1,1]
target = 0
def search(nums,target):
    def binS(nums,target,low,high):
        while low<=high:
            mid=(low+high)//2
            if nums[mid]==target:
                return True
            elif target<nums[mid]:
                high=mid-1
            else:
                low=mid+1
        return False
    if len(nums)==1 and target==nums[0]:
        return True
    elif len(nums)==1:
        return False
    if nums[0]>=nums[-1]:
        idx=nums.index(max(nums))
        if nums[idx+1]<nums[idx]:
            idx=nums.index(max(nums))
        else:
            while nums[idx+1]>=nums[idx]:
                

                idx+=1
                if idx==len(nums)-1:
                    break
                    



       
        if target<nums[0]:
            return binS(nums,target,idx+1,len(nums)-1)
        else:
            
            return binS(nums,target,0,idx)
        
    else:
        return binS(nums,target,0,len(nums)-1)
print(search(nums,target))