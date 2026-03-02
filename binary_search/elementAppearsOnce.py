
def singleNonDuplicate(nums):
    low, high = 0, len(nums) - 1
    
    while low < high:
        mid = (low + high) // 2
        
        # make mid even
        if mid % 2 == 1:
            mid -= 1
        
        if nums[mid] == nums[mid + 1]:
            low = mid + 2
        else:
            high = mid
    
    return nums[low]
print(singleNonDuplicate(nums = [1,1,2,3,3,4,4,8,8]))