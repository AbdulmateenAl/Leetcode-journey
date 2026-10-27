class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        # The Brute-force solution
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] > nums[j]:
                    tmp = nums[j]
                    nums[j] = nums[i]
                    nums[i] = tmp
        
        return nums