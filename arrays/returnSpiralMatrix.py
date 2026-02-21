import numpy as np
matrix = [[1,2,3],[4,5,6],[7,8,9]]
m=0
n=len(matrix[0])
matrix=np.array(matrix)
m1=matrix[0]
print(f"m1",m1)
m+=1
matrix=matrix[m:,:]
print(f"first row removed",matrix)

m2=matrix[:,-1]
print(f"m2",m2)
n-=1
matrix=matrix[:,0:n]
print(matrix)
m3=matrix[-1]


print(f"This is m3 reversed",np.flip(m3))
m+=1
matrix=matrix[m:,:]
print(f"last row removed",matrix)


