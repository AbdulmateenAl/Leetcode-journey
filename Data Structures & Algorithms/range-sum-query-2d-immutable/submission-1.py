class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix

        row, col = len(matrix), len(matrix[0])
        self.prefix_sum = [[0] * (col + 1) for _ in range(row + 1)]

        for i in range(1, len(self.prefix_sum)):
            sum = 0
            for j in range(1, len(self.prefix_sum[0])):
                # sum += matrix[i - 1][j - 1] + self.prefix_sum[i][j - 1]
                level = i
                while level:
                    sum += matrix[level - 1][j - 1]
                    level -= 1

                self.prefix_sum[i][j] = sum


    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        bottomRight = self.prefix_sum[row2 + 1][col2 + 1]
        topRight = self.prefix_sum[row1][col2 + 1]
        bottomLeft = self.prefix_sum[row2 + 1][col1]
        topLeft = self.prefix_sum[row1][col1]
        
        return bottomRight - topRight - bottomLeft + topLeft


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)