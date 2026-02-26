def maxProdt(nums):
    res=nums[0]

    maxEnd=nums[0]

    for i in range(1,len(nums)):
        maxEnd=max(maxEnd*nums[i],nums[i])

        res=max(res,maxEnd)

    return res
nums = [-2,3,-4]
print(maxProdt(nums))

