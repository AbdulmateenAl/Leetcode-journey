class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        i = 0

        for num in nums:
            diff = target - num
            nums[i] = None

            if diff in nums:
                return [i, nums.index(diff)]

            i += 1