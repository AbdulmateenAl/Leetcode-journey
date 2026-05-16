class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # Using hashmaps
        mp = defaultdict(int)
        for i in range(len(numbers)):
            diff = target - numbers[i]
            if diff in mp:
                return [mp[diff], i + 1]
            mp[numbers[i]] = i + 1