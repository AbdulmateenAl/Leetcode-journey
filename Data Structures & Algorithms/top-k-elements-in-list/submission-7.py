class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = defaultdict(int)

        for num in nums:
            freq[num] = 1 + freq.get(num, 0)

        sorted_freq = [k for k, v in sorted(freq.items(), key = lambda item:item[1])]

        return sorted_freq[-k:]