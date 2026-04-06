class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()

        for i in range(len(nums)):
            if nums[i] > 0:
                break

            if i > 0 and nums[i] == nums[i - 1]:
                continue

            pairs = self.sum_pairs_sorted(nums, i + 1, -nums[i])

            for pair in pairs:
                result.append([nums[i]] + pair)

        return result

    def sum_pairs_sorted(self, nums: List[int], start: int, target: int) -> List[List[int]]:
        left, right = start, len(nums) - 1
        pairs = []

        while left < right:
            sum = nums[left] + nums[right]

            if sum == target:
                pairs.append([nums[left], nums[right]])
                left += 1
                while left < right and nums[left] == nums[left -1]:
                    left += 1
            elif sum < target:
                left += 1
            else:
                right -= 1

        return pairs