arr = [3, 5, 6, 8] 
k = 7

count=0
i,j=0,len(arr)-1
        
while i<j:
                
        
    if (arr[i]^arr[j])<k:
        count+=1
    else:
        i+=1
        j-=1
print(count)






