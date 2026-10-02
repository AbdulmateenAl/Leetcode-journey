class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        contains = {}

        for i in range(len(nums)):
            if nums[i] in contains:
                return nums[i]
            contains[nums[i]] = i