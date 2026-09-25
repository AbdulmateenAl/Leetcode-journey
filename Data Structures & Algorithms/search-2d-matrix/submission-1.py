class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        for row in matrix:
            l, r = 0, len(row) - 1

            if target == row[l]:
                return True
            elif target < row[l] or target > row[r]:
                continue
            
            while l <= r:
                mid = l + ((r - l) // 2)
                if target == row[mid]:
                    return True
                elif target > row[mid]:
                    l = mid + 1
                else:
                    r = mid -1

        return False