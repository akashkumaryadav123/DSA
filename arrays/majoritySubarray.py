nums=[1,2,-1,-2,2,1,-2,1,4,-5,4]
max_value=float('-inf')


for st in range(0,len(nums)):
    cs=0
    for end in range(st,len(nums)):
        cs+=nums[end]
        max_value=max(cs,max_value)
        
           
print(max_value)
            
