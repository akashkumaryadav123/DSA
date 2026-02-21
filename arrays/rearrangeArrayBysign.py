nums = [-1,1]
n=len(nums)
positive_nums=[]
negative_nums=[]
for i in nums:
    if i>0:
        positive_nums.append(i)
        
    else:
        negative_nums.append(i)
j=0
final_nums=[0]*n
for i in range(0,n,+2):
    final_nums[i]=positive_nums[j]
    j+=1
j=0
for i in range(1,n,+2):
    final_nums[i]=negative_nums[j]
    j+=1



print(positive_nums,negative_nums)
print(final_nums)