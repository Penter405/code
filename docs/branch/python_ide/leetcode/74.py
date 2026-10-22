class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        my=len(matrix)
        mx=len(matrix[0])
        def formating(n):

            return n//mx,n%mx
        left=0
        right=my*mx-1

        while left<=right:
            mid=(left+right)//2
            y,x=formating(mid)
            if matrix[y][x]>=target:
                right=mid-1
            elif matrix[y][x]<target:
                left=mid+1
        y,x=formating(left)
        if left<0 or left>my*mx-1:
            return False
        return matrix[y][x]==target
matrix = [[1]]
target = 2
print(Solution.searchMatrix(None,matrix,target))