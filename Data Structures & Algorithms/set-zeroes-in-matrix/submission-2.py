class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        # m is length of rows while n is length of columns
        m, n = len(matrix), len(matrix[0])
        zero_rows, zero_cols = set(), set()

        # Pass 1: Traverse through the matrix and get the rows and column containing zero
        for r in range(m):
            for c in range(n):
                num = matrix[r][c]

                if num == 0:
                    zero_rows.add(r)
                    zero_cols.add(c)

        # Pass 2: Set any cell to zero if the row is in 'zero_rows' or the column is in 'zero-cols'
        for r in range(m):
            for c in range(n):
                if c in zero_cols or r in zero_rows:
                    matrix[r][c] = 0