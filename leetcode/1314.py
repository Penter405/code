class Solution:
    def matrixBlockSum(self, mat: list[list[int]], k: int) -> list[list[int]]:
        matrix=mat
        y_size=len(matrix)
        x_size=len(matrix[0])
        prefix=[[0 for _ in range(x_size+1)] for _ in range(y_size+1)]#1 index
        result=[[0 for _ in range(x_size)] for _ in range(y_size)]#0 indexed
        for y in range(1,y_size+1):
            for x in range(1,x_size+1):
                by=y-1
                bx=x-1
                prefix[y][x]=matrix[by][bx]+prefix[y-1][x]+prefix[y][x-1]-prefix[y-1][x-1]
        def get(y,x,k):#0 indexed
            nonlocal y_size , x_size
            x1=x-k
            x2=x+k
            y1=y-k
            y2=y+k
            #1 indexed
            x1+=1;x2+=1;y1+=1;y2+=1
            result=prefix[min(y2,y_size)][min(x2,x_size)]
            result-=prefix[max(0,y1-1)][min(x2,x_size)]
            result-=prefix[min(y2,y_size)][max(x1-1,0)]
            result+=prefix[max(y1-1,0)][max(x1-1,0)]
            return result
        for y in range(y_size):
            for x in range(x_size):
                result[y][x]=get(y,x,k)
        return result

        