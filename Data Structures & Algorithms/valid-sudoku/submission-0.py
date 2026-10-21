class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        las=["1", "2", "3", "4", "5", "6", "7", "8", "9"]
        for row in board:
            seen=set()
            for cell in row:
                if cell==".":
                    continue
                if cell in seen: 
                    return False
                seen.add(cell)
        for c in range(9):
            seen=set()
            for r in range(9):
                cell=board[r][c]
                if cell==".":
                    continue
                if cell in seen:
                    return False
                seen.add(cell) 
        d={}
        for c in range (9):
            for r in range(9):
                cell=board[r][c]
                if cell==".":
                    continue
                key=(c//3,r//3)
                if key not in d:
                    d[key]=set()
                if cell in d[key]:
                    return False
                d[key].add(cell)
        return True
            

            


        