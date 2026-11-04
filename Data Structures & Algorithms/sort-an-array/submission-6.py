class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        minVal = min(nums)
        maxVal = max(nums)

        counter = defaultdict(int)
        for num in nums:
            counter[num] += 1

        index = 0
        for i in range(minVal, maxVal + 1):
            while counter[i]:
                nums[index] = i
                index += 1
                counter[i] -= 1

        return nums