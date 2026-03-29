def arrange(s:str):
    if len(s)==0:
        return 
    map={}
    for i in s :
        map[i]=map.get(i,0)+1
    dict_sort=dict(sorted(map.items(),key=lambda x:x[1],reverse=True))
    s_f=""
    for i in dict_sort:
        s_f+=i*dict_sort[i]

    return (s_f)
    
print(arrange("tree"))
