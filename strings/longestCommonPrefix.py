def findPeak(strs):

    a=1
    if len(strs)==1:
        return strs[0]
    elif len(strs)==0:
        return ""
    

    while a<=len(strs[0]):
       
        
        cp=strs[0][:a]
        
        
        for s in strs[1:]:
           
            
            if s[:a]!=cp:
                return strs[0][:a-1]
                
        a+=1
    return strs[0][:a-1]
print(findPeak(strs = ["ab", "ab"]))
            
    

