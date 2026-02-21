matrix = [[1,1,1],[1,0,1],[1,0,1]]
m=3
n=3
zero_index=[[i, j]
 for i, row in enumerate(matrix)
 for j, val in enumerate(row)
 if val == 0]
print(zero_index)
print(matrix)

for i in range(len(zero_index)):
    s=zero_index[0][0]
    e=zero_index[0][1]

    for x in range(m):
        for y in range(n):
            if x==s or y==e:
                matrix[x][y]=0
    zero_index.pop(0)
print(matrix)
            




