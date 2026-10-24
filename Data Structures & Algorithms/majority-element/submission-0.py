class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = {}
        for num in nums:
            count[num] = 1 + count.get(num, 0)

        maxCount = -1
        maxNum = 0
        for num in count:
            if count[num] > maxCount:
                maxCount = count[num]
                maxNum = num

        return maxNum