class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows = len(board)
        cols = len(board[0])

        def backtrace(r, c, index):
            if index == len(word):
                return True

            if r < 0 or r >= rows or c < 0 or c >= cols:
                return False

            if board[r][c] != word[index] or board[r][c] == "#":
                return False

            temp = board[r][c]
            board[r][c] = "#"
            result = (backtrace(r+1, c, index+1) or
            backtrace(r-1, c, index+1) or 
            backtrace(r, c+1, index+1) or
            backtrace(r, c-1, index+1) )

            board[r][c] = temp
            return result 

        for r in range(rows):
            for c in range(cols):
                if backtrace(r, c, 0):
                    return True
        
    
        return False
