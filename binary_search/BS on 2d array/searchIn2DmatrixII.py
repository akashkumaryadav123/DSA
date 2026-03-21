def Bsearch(matrix,target):
    m,n=len(matrix),len(matrix[0])
    row=0
    col=n-1
    
    while row<=col:
        current=matrix[row][col]
        if target==current:
            return True
        elif target<current:
            col-=1
        else:
            row+=1
    return False



print(Bsearch(matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], target = 4))