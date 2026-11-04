class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        bucket = [0] * 3
        for i in range(len(nums)):
            bucket[nums[i]] += 1

        index = 0
        for b in range(len(bucket)):
            for c in range(bucket[b]):
                nums[index] = b
                index += 1