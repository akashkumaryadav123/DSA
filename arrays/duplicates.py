arr=[1,2,2,4,3,7,4]
n=len(arr)
freq={}
for num in arr:
    if num in freq:
        freq[num]+=1
    else:
        freq[num]=1
print(freq)
duplicates
freq_list=[[k,v] for k,v in freq.items()]
print(freq_list)
        
