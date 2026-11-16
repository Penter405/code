class NumMatrix:

    def __init__(self, matrix: list[list[int]]):#x,y = math
        #matrix=matrix[0]
        self.y_size=len(matrix)
        self.x_size=len(matrix[0])
        self.prefix=[[0 for _ in range(self.x_size+1)] for _ in range(self.y_size+1)]
        for y in range(1,self.y_size+1):
            for x in range(1,self.x_size+1):
                by=y-1
                bx=x-1
                self.prefix[y][x]=matrix[by][bx]+self.prefix[y-1][x]+self.prefix[y][x-1]-self.prefix[y-1][x-1]
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        #row=x
        #col=y
        row1+=1;col1+=1;row2+=1;col2+=1
        result=self.prefix[row2][col2]
        result-=self.prefix[row1-1][col2]
        result-=self.prefix[row2][col1-1]
        result+=self.prefix[row1-1][col1-1]
        return result

action=["NumMatrix", "sumRegion", "sumRegion", "sumRegion"]
data=[[[[3, 0, 1, 4, 2], [5, 6, 3, 2, 1], [1, 2, 0, 1, 5], [4, 1, 0, 1, 7], [1, 0, 3, 0, 5]]], [2, 1, 4, 3], [1, 1, 2, 2], [1, 2, 2, 4]]
for a ,d in zip(action,data):
    if a=="NumMatrix":
        penter=NumMatrix(d)
    else:
        print(penter.sumRegion(*d))


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)