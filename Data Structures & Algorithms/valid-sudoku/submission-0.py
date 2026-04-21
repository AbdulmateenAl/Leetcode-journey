class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_sets = [set() for _ in range(9)] # Hash set for rows
        col_sets = [set() for _ in range(9)] # Hash set for columns
        subgrid_sets = [[set() for _ in range(3)] for _ in range(3)]

        # Loop through the 9x9 board
        for r in range(9):
            for c in range(9):
                num = board[r][c]
                if num == '.':
                    continue # This ignores the empty boxes in the board

                if num in row_sets[r]:
                    return False
                elif num in col_sets[c]:
                    return False
                elif num in subgrid_sets[r // 3][c // 3]:
                    return False

                # To add numbers to our hash set
                row_sets[r].add(num)
                col_sets[c].add(num)
                subgrid_sets[r // 3][c // 3].add(num)

        return True