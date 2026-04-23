class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        test = [[matrix[r][c] for c in range(len(matrix[0]))] for r in range(len(matrix))]

        for r in range(len(test)):
            for c in range(len(test[0])):
                num = matrix[r][c]

                if num == 0:
                    test[r] = [0] * len(test[0]) # Sets row to zero

                    # Sets columns to zero
                    for sub_r in range(len(test)):
                        for sub_c in range(len(test[0])):
                            if c == sub_c:
                                test[sub_r][sub_c] = 0

        for r in range(len(test)):
            for c in range(len(test[0])):
                matrix[r][c] = test[r][c]