class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # I want to make this solution go in one pass
        # So, what I will be doing is to store numbers in the array
        # as I am checking for the difference in a single loop
        hash_map = {}

        for i, a in enumerate(nums):
            diff = target - a
            if diff in hash_map:
                return [hash_map[diff], i]
            hash_map[a] = i