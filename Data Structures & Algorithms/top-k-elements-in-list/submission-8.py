class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {} # Holds the unique numbers and frequencies

        for num in nums:
            count[num] = 1 + count.get(num, 0)

        freq_heap = [] # Holds maximum of k numbers
        for key, value in count.items():
            heapq.heappush(freq_heap, (value, key))

            if len(freq_heap) > k:
                heapq.heappop(freq_heap)

        res = []
        for v, k in freq_heap:
            res.append(k)

        return res