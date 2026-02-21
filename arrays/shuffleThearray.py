nums = [2,5,1,3,4,7]
n = 3
ans=[0]*2*n
print(ans)
j=0
for i in range(0,n+2,+2):
    ans[i]=nums[j]
    ans[i+1]=nums[n +j]
    print(ans)
    j+=1

print(ans)