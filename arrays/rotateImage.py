matrix = [[1,2,3],[4,5,6],[7,8,9]]
n=len(matrix)
#transpose
for i in range(n):
    for j in range(i+1,n):
        matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
print(matrix)
#reverse
for i in range(n):
    matrix[i].reverse()
print(matrix)





# rotated=[[0 for i in range(n)]for j in range(n)]

# k=0

    
# j=0
# for i in range(n-1,-1,-1):
#     print("Next")
#     for j in range(n):
#         print(f"Im i",i)
#         print(f"Im j",j)
#         print(f"Im k",k)
#         rotated[j][k]=matrix[i][j]
            
#         j+=1
#     k+=1   
# print(f"Im rotated: ",rotated)
