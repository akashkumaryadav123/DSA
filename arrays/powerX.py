n=10
x=2.00
binform=n;
ans=1
if n<0:
    x=1/x
    binform=-n
while binform>0:
    if binform%2==1:
        ans*=x
    x*=x
    binform//=2
print(ans)
