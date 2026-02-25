nums=[1,2,1,2,1]
k = 3
count=0
ps=[0]*len(nums)
ps[0]=nums[0]
for i in range(1,len(nums)):
    ps[i]=ps[i-1]+nums[i]
print(ps)

m={}
for j in range(0,len(nums)):
    if ps[j]==k:
        count+=1
    val=ps[j]-k
    if val in m:
        count+=m[val]
    
    m[ps[j]] = m.get(ps[j], 0) + 1
print(m)
print(count)


