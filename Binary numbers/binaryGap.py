n=15
n=format(n,"b")
count=0
if n==0 or str(n).count("1")==1:
    print(0)

for i in range(len(n)):
    
    for j in range(i+1,len(n)):
        if n[i]=="1" and n[j]=="1":
            if (j-i)>count:
                print(i,j)
                count=(j-i)
            break
print(count)
