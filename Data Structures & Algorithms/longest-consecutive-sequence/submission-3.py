class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        values = defaultdict(int)
        highest = float('-inf')

        for i, num in enumerate(nums):
            values[num] = i

        for key in values:
            count = 1
            nxt = key + 1
            while nxt in values:
                count += 1
                nxt += 1
            
            highest = max(highest, count)

        return highest