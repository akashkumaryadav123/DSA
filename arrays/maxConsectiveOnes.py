

nums = [1,0,1,1,0,1]
hash_dict={}
x=0
char=97
for i in range(len(nums)):
    
    if nums[i]==1:
        x+=1
    if nums[i]!=1 or i==len(nums)-1:
        
        hash_dict[chr(char)]=x
        x=0
        char+=1
print(hash_dict)
print(max(hash_dict.values()))




