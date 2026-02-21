nums=[23,12,9,52,20,57]
n=len(nums)
for i in range(n-1):
    min_ind=i
    for j in range(i+1,n):
        if nums[j]<nums[min_ind]:
            min_ind=j
    nums[i],nums[min_ind]=nums[min_ind],nums[i]
print(nums)


    