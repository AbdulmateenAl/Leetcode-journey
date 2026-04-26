class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        # m is length of rows while n is length of columns
        m, n = len(matrix), len(matrix[0])
        first_col_has_zero, pos_col = False, set()
        first_row_has_zero, pos_row = False, set()

        # Checks the first column for zero
        for r in range(m):
            if matrix[r][0] == 0:
                pos_col.add(r)
                first_col_has_zero = True

        # Checks the first row for zero
        for c in range(n):
            if matrix[0][c] == 0:
                pos_row.add(c)
                first_row_has_zero = True

        # For the step below, we want to traverse through the sub-matrix(which is the matrix 
        # without the first row and the first column) and check for zeros. If a zero is found
        # we set the first column(above it) and row(leftmost) to zero.
        for r in range(1, m):
            for c in range(1, n):
                if matrix[r][c] == 0:
                    # Sets the topmost and leftmost to zero when zero is encountered
                    matrix[0][c] = 0
                    matrix[r][0] = 0


        # Now we check the sub matrix for zero and if the corresponding topmost
        # has a zero, we give the entire column a zero. And if the leftmost has
        # a zero we give the entire row a zero.
        for r in range(1, m):
            for c in range(1, n):
                if matrix[r][c] == 0 and matrix[0][c] == 0 and matrix[r][0] == 0:
                    matrix[r] = [0] * n # Sets the row to zero

                    # Sets the columns to zero
                    for sub_r in range(m):
                        matrix[sub_r][c] = 0



        # Then, if the first column or second column initially had zero, we set the column
        # or the row to zero
        if first_row_has_zero:
            matrix[0] = [0] * n # Sets the first row to zero if 'first_row_has_zero' is true

            # For the column
            for i in pos_row:
                for r in range(m):
                    matrix[r][i] = 0

        if first_col_has_zero:
            # Sets the first column to zero if 'first_col_has_zero' is true
            for r in range(m):
                matrix[r][0] = 0

            # For the row
            for i in pos_col:
                matrix[i] = [0] * n