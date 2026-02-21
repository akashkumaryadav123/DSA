#divide into smaller elemnets
#merge back to sorted subarray
def merge(arr,st,mid,end):
    temp=[]
    i=st
    j=mid+1
    while(i<=mid and j<=end):
        if arr[i]<=arr[j]:
            temp.append(arr[i])
            i+=1
        else:
            temp.append(arr[j])
            j+=1
    while i<=mid:
        temp.append(arr[i])
        i+=1
    while j<=end:
        temp.append(arr[j])
        j+=1
    for i in range(len(temp)):
        arr[(st+i)]=temp[i]



def mergeSort(arr,st,end):
    mid=st+(end-st)//2
    if st<end:
        mergeSort(arr,st,mid)
        mergeSort(arr,mid+1,end)
        merge(arr,st,mid,end)
arr=[2,42,1,2,7]
mergeSort(arr,0,len(arr)-1)
print(arr)