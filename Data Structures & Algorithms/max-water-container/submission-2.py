class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        max_amount = 0

        while l < r:
            min_height = min(heights[l], heights[r])
            total = min_height * (r - l)
            max_amount = max(max_amount, total)

            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1

        return max_amount