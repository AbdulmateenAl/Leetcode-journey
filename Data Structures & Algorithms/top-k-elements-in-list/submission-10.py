class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Using Bucket Sort
        count = {} # Holds unique numbers and their frequencies
        for num in nums:
            count[num] = 1 + count.get(num, 0)

        freq_group = defaultdict(list) # freq_group[i] holds numbers with frequency i
        for key, value in count.items():
            freq_group[value].append(key)

        sorted_freq_group = sorted(freq_group, reverse=True) # Sorts freq_group and returns a sorted list
        res = []
        for item in sorted_freq_group:
            res += freq_group[item]

        return res[:k]