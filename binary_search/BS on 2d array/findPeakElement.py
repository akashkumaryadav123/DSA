def findPeakGrid(mat: list) -> list:
    m,n=len(mat),len(mat[0])
    def get_max_col(col):
        max_row=0
        for r in range(m):
            if mat[r][col]>mat[max_row][col]:
                max_row=r
        return max_row
    low,high=0,n-1
    while low<=high:
        mid=(low+high)//2
        max_row=get_max_col(mid)
        left_neighbour=mat[max_row][mid-1] if mid-1>=0 else -1
        right_neighbour=mat[max_row][mid+1] if mid+1<n else -1
        current=mat[max_row][mid]
        if current>left_neighbour and current>right_neighbour:
            return [max_row,mid]
        if current<left_neighbour:
            high=mid-1
        else:
            low=mid+1
    return None
print(findPeakGrid(mat = [[1,4],[3,2]]))