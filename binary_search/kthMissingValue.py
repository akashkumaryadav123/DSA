def findKthPositive(arr, k):
   low, high = 0, len(arr) - 1
   while low <= high:
       mid = (low + high) // 2
       missing = arr[mid] - (mid + 1)
       if missing >= k:
           high = mid - 1
       else:
           low = mid + 1
   return k + low

arr = [2, 3, 4, 7, 11]
k = 5
print(findKthPositive(arr, k)) 