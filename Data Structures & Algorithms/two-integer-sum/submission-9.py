class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # [2,5,1,6,9,1], t=10
        # Firstly, we store all values and index in a hashmap
        # but if we have duplicate we will only have the last duplicate
        # We start from the first index, get the difference and check if the difference is in the hashmap
        # If it is, we return the current index and the index in the hashmap
        # else, we continue till we get our value
        # And if we eventually don't get our values, we just simply return an empty list

        hash_map = {}
        # Store all values in a hashmap.
        # But if duplicates, stores the value of the last duplicate
        for i, a in enumerate(nums):
            hash_map[a] = i

        for i, a in enumerate(nums):
            diff = target - a
            if diff in hash_map and i != hash_map[diff]:
                return [i, hash_map[diff]]

        return []