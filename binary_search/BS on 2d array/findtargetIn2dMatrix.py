def searchMatrix( matrix, target: int) -> bool:
    m=len(matrix)
    n=len(matrix[0])
    low=0
    high=m*n-1
    print(f"low {low} high {high}")
    while low<=high:
        mid=(low+high)//2
        print(f"mid {mid}")
        row=(mid//n)
        col=(mid%n)
        print(f"row {row} col {col}")
        if target==matrix[row][col]:
            return True
        elif target >matrix[row][col]:
            low=mid+1
        else:
            high=mid-1

    return False
print(searchMatrix(matrix=[[1,1]],target=2))
        