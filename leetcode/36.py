class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row=[set() for _ in range(9)]
        col=[set() for _ in range(9)]
        box=[[set() for _ in range(3)] for _ in range(3)]
        #print(row)
        #print(col)
        #print(box)
        
        #print(id(row[0]))
        #print(id(row[1]))
        #print(id(row[0])==id(row[1]))
        #return False
        index_r=-1
        for r in board:
            index_r+=1
            index_c=-1
            for c in r:
                index_c+=1
                print(index_r,index_c,c)
                if c=='.':
                    continue
                if not(c in row[index_r] or c in col[index_c] or c in box[index_r//3][index_c//3]):
                    row[index_r].add(c)
                    col[index_c].add(c)
                    box[index_r//3][index_c//3].add(c)
                else:
                    print(c)
                    print(c in row[index_r])
                    print(c in col[index_c])
                    print(c in box[index_r//3][index_c//3])
                    print(row)
                    print(col)
                    print(box)
                    print("bad")
                    return False
        return True