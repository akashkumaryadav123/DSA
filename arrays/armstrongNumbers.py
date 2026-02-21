n=372
n_string=str(n)
sum=0
for i in range(len(n_string)):
    sum+=int(n_string[i])**3
print(sum)
if sum==n:
    print("True")
else:
    print("False")