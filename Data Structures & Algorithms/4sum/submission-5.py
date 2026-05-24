class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        # Brote-force solution
        n = len(nums)
        nums.sort() # Sorts the numbers in ascending order
        res = set() # Using a set to get unique groups

        for i in range(n - 3):
            for j in range(i + 1, n - 2):
                for k in range(j + 1, n - 1):
                    for l in range(k + 1, n):
                        total = nums[i] + nums[j] + nums[k] + nums[l]
                        # Checks if it is equal to the target, then adds it to our result
                        if total == target:
                            res.add((nums[i], nums[j], nums[k], nums[l]))

        return list(res) # Converts the set to a list/array