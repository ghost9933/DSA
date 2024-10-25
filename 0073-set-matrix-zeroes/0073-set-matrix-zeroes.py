class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        if not matrix or not matrix[0]:
            return matrix
        
        rows=len(matrix)
        cols=len(matrix[0])
        # First pass: find all the rows and columns that need to be zeroed
        is_col=False
        for i in range(rows):
            if matrix[i][0] == 0:
                is_col = True
            for j in range(1,cols):
                if matrix[i][j] == 0:
                    matrix[i][0]=0
                    matrix[0][j]=0
        for x in matrix:
            print(x)
        for i in range(1, rows):
            for j in range(1, cols):
                if not matrix[i][0] or not matrix[0][j]:
                    matrix[i][j] = 0

        # See if the first row needs to be set to zero as well
        if matrix[0][0] == 0:
            for j in range(cols):
                matrix[0][j] = 0

        # See if the first column needs to be set to zero as well
        if is_col:
            for i in range(rows):
                matrix[i][0] = 0
       
        return matrix