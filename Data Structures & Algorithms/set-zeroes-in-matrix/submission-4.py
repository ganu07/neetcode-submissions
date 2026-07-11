class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        
        rows = len(matrix)
        cols = len(matrix[0])
        rows_zero = set()
        cols_zero = set()


        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == 0:
                    rows_zero.add(i)
                    cols_zero.add(j)
        
        for i in range(rows):
            for j in range(cols):
                if i in rows_zero or j in cols_zero:
                    matrix[i][j] = 0
        



        