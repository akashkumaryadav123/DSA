def romanTointeger(s:str):
    dict={"I":1,"V" :5,"X":10,"L":50,"C":100,"D":500,"M":1000,"IV":4,"IX":9,"XL":40,"XC":90,"CD":400,"CM":900}
    l=["IV","IX","XL","XC","CD","CM"]

    integer=0
    i=0
    while i<=(len(s)-1):
       
        if i !=len(s)-1:
            if s[i]+s[i+1] in l:
                integer+=dict[s[i]+s[i+1]]
                i+=2
                continue
            


        if s[i] in dict:
            
            integer+=dict[s[i]]
            i+=1
        
    return integer
print(romanTointeger("III"))

