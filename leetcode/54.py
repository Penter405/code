class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        result=[]
        while matrix:
            for rs in (matrix.pop(0)):
                result.append(rs)
            matrix=[list(row) for row in zip(*matrix)][::-1]
        return result