class Solution:
    def minimumTotal(self, triangle: list[list[int]]) -> int:
        """
        for every node, its child is from above layer get the index self-1 and self on the above layer
        """

        children=list()
        rows=len(triangle)
        dp=[[0]*(r+1) for r in range(rows)]
        print(dp)
        
        def cin(row,column):
            if row<0 or column<0:
                return 0
            if column>row:
                return 0
            children.append(dp[row][column])
            return 0
        for row in range(rows):
            for column in range(row+1):
                children.clear()
                for a,b in [(-1,-1),(-1,0)]:
                    cin(row+a,column+b)
                
                if len(children)==0:
                    dp[row][column]=triangle[row][column]
                else:
                    dp[row][column]=triangle[row][column]+min(children)
        for rs in dp:
            print(rs)
        return min(dp[-1])