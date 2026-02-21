nums = [1,2,4]
k = 5
for i in range(len(nums)-1):
    if (nums[i+1]-nums[i])<=5:
        nums[i]+=nums[i+1]-nums[i]
    k-=nums[i+1]-nums[i]
    