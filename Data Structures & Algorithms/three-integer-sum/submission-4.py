class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []

        nums.sort() # Sorts the array in ascending order

        for i in range(len(nums)):
            if nums[i] > 0:
                break
            
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            pairs = self.pair_sum_sorted(nums, (i + 1), -nums[i])
            result.extend([[nums[i]] + arr for arr in pairs])

        return result
    
    def pair_sum_sorted(self, nums: List[int], start: int, target: int) -> List[list[int]]:
        left, right = start, len(nums) - 1
        pairs = []

        while left < right:
            two_sum = nums[left] + nums[right]
            
            if two_sum == target:
                pairs.append([nums[left], nums[right]])
                left += 1
                while left < right and nums[left] == nums[left - 1]:
                    left += 1
            elif two_sum < target:
                left += 1
            else:
                right -= 1

        return pairs
