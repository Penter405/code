class Solution():
    def __init__(self):
        pass
    def solveNQueens(self,n:int):
        """
        n=board size
        """
        result=0
        r_board=[]
        board=[["."]*n for _ in range(n)]
        went=[]
        #bad=False
        def is_legal(a:list,b:list):
            if a[1]+b[0]-a[0]==b[1] or a[1]-b[0]+a[0]==b[1]:
                return False
            if a[0]==b[0] or a[1]==b[1]:
                return False
            return True
        """
        print(is_legal([0,0],[3,3]))
        print(is_legal([3,3],[0,0]))
        print(is_legal([3,3],[0,1]))
        """
        def backtracking(row=0,column=0):
            nonlocal went,n,result,r_board
            for rs in range(row):
                if not is_legal([row,column],[rs,went[rs]]):
                    #print([row,column],[rs,went[rs]])
                    return 0
            #backtracking main
            went.append(column)
            board[row][column]='Q'
            if row==n-1:
                #print(row,column)
                #print("more")
                result+=1
                r_board.append(["".join(rs) for rs in board])
                board[row][column]='.'
                went.pop(-1)
                return 0
            

            for rs in range(n):
                backtracking(row+1,rs)

            #backtracking end
            went.pop(-1)
            board[row][column]='.'

            return 0
        for rs in range(n):
            backtracking(column=rs)
            #print("log",board)
        return r_board



Penter=Solution()
n=int(input())
print(Penter.get_queen(n))