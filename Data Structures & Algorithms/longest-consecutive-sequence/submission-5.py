class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        values = defaultdict(int)
        highest = 0

        for i, num in enumerate(nums):
            if (num - 1) not in nums:
                values[num] = i

        for key in values:
            count = 1
            nxt = key + 1
            while nxt in nums:
                count += 1
                nxt += 1
            
            highest = max(highest, count)

        return highest