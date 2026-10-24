class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = {}
        maxFreq = -1
        maxNum = 0
        for num in nums:
            count[num] = 1 + count.get(num, 0)

            if count[num] > maxFreq:
                maxFreq = count[num]
                maxNum = num

        return maxNum