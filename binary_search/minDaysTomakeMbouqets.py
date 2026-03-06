bloomDay = [7,7,7,7,12,7,7]
m = 2
k = 3
def minDays(bloomday,m,k):

    def adjcheck(bloomDay,day,m,k):
        res=0
        s=0
        for b in bloomDay:
            if day>=b:
                res+=1
                if res>=k:
                    print("res : ",res)
                    s+=1
                    res=0
            else:
                res=0
        return s>=m
    l=min(bloomDay)
    r=max(bloomDay)
    while l<=r:
        mid=(l+r)//2
        if adjcheck(bloomDay,mid,m,k):
            r=mid-1
        else:
            l=mid+1
    return l

    

print(minDays(bloomDay,m,k))

