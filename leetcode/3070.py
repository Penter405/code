List=list
class Solution:
    def countSubmatrices(self, grid: List[List[int]], k: int) -> int:
        result=0
        matrix=grid
        self.y_size=len(matrix)
        self.x_size=len(matrix[0])
        self.prefix=[[0 for _ in range(self.x_size+1)] for _ in range(self.y_size+1)]
        for y in range(1,self.y_size+1):
            for x in range(1,self.x_size+1):
                by=y-1
                bx=x-1
                self.prefix[y][x]=matrix[by][bx]+self.prefix[y-1][x]+self.prefix[y][x-1]-self.prefix[y-1][x-1]
                if self.prefix[y][x]<=k:
                    result+=1
        return result