op=0
nums = [4,1,3]
k = 4

if sum(nums)<k:
    print("Output : ",sum(nums))
elif sum(nums)>k:
    i=nums.index(max(nums))
    while sum(nums)%k!=0:
        nums[i]-=1
        op+=1

else:
    print(op)
print(op)

