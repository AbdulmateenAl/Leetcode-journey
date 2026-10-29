class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        # Quick-sort
        if len(nums) < 1:
            return []
        mid = (0 + len(nums) - 1) >> 1
        l = []
        r = []
        eq = []

        for num in nums:
            if num < nums[mid]:
                l.append(num)
            elif num > nums[mid]:
                r.append(num)
            else:
                eq.append(num)
        
        return [*self.sortArray(l), *eq, *self.sortArray(r)]