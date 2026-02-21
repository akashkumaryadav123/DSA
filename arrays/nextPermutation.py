nums=[3,2,1]


for i in range(len(nums) - 1, -1, -1):
    print(i)
    if nums[i]>nums[i-1]:
        pivot=nums[i-1]
        break

print(pivot)
pivot_ind=nums.index(pivot)
print("index of piviot : ", pivot_ind)
if pivot_ind==len(nums)-1:
    print(nums.sort())

#swapping with just greater than pivot 
else:

    nums[pivot:]=sorted(nums[pivot:])
    nums[pivot_ind],nums[pivot_ind+1]=nums[pivot_ind+1],nums[pivot_ind]
    print(nums)
 



