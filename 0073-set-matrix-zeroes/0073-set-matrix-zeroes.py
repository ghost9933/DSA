class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        if not matrix or not matrix[0]:
            return matrix
        
        rows = len(matrix)
        cols = len(matrix[0])
        
        zero_rows = set()
        zero_cols = set()
        
        # First pass: find all the rows and columns that need to be zeroed
        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == 0:
                    zero_rows.add(i)
                    zero_cols.add(j)
        
        # Second pass: zero out the marked rows
        for i in zero_rows:
            for j in range(cols):
                matrix[i][j] = 0
        
        # Zero out the marked columns
        for j in zero_cols:
            for i in range(rows):
                matrix[i][j] = 0
        
        return matrix