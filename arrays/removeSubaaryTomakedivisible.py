nums = [6,3,5,2]
p = 9
sum1=0
a=0
if (sum(nums)%p) in nums:
    a+=1
else:

    for i in range(len(nums)):
        sum1+=nums[i]
        if sum1%p==0:
            a=i
print(a)
    


