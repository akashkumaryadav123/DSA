def shipWithinDays(weights,days):
    def check(weights,days,mid):
        t_w=0
        t_d=1
        for w in weights:
            

            if t_w+w>mid:
                t_w=0
                
                t_d+=1
            t_w+=w
                
        return t_d<=days
    l=max(weights)
    r=sum(weights)
    
    while l<=r:
        mid=(l+r)//2
        print("Im mid ",mid)
        if check(weights,days,mid):
            r=mid-1
            print("this is r : ",r)
        else:
           
            l=mid+1
            print("this is l : ",l)
    return l
print(shipWithinDays(weights = [1,2,3,1,1], days = 4))


