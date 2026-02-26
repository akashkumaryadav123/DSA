nums = [1,3,5,6]
target = 7
low=0
high=len(nums)-1
while low<=high:
    mid=(low+high)//2
    if nums[mid]==target:
        print(mid)
    elif target>nums[mid]:
        low=mid+1
    else:
        low=mid-1
if target>nums[0]:
    print(low)
else:
    print(mid)