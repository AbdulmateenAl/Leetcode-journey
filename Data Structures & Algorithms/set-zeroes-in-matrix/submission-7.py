class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        # In-place solution

        m, n = len(matrix), len(matrix[0])

        first_row_has_zero = any(matrix[0][c] == 0 for c in range(n)) # Returns true if condition is met
        first_col_has_zero = any(matrix[r][0] == 0 for r in range(m)) # Returns true if condition is met

        # Traverse through the sub-matrix and mark the first row and column with zero if zero is met
        for r in range(1, m):
            for c in range(1, n):
                if matrix[r][c] == 0:
                    matrix[0][c] = 0 # Sets the first row above it to zero
                    matrix[r][0] = 0 # Sets the first column left-most to zero

        # Traverse through the sub-matrix again and set zero
        # if either the first row or column of a cell is zero
        for r in range(1, m):
            for c in range(1, n):
                if matrix[0][c] == 0 or matrix[r][0] == 0:
                    matrix[r][c] = 0

        if first_row_has_zero:
            # matrix[0] = [0] * n # or
            for c in range(n):
                matrix[0][c] = 0

        if first_col_has_zero:
            for r in range(m):
                matrix[r][0] = 0