nums = [1, 2, 2, 1, 3]
n=len(nums)
freq={}
for num in nums:
    if num in freq:
        freq[num]+=1
    else:
        freq[num]=1
freq_list=[[k,v] for k,v in freq.items()]
print(freq_list)


