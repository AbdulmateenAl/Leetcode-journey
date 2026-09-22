class Solution:
    def pair_2sum(self, numbersLeft: List[int], target: int) -> List[List[int]]:
        output = []
        l, r = 0, len(numbersLeft) - 1
        
        while l < r:
            if numbersLeft[l] + numbersLeft[r] == target:
                output.append([numbersLeft[l], numbersLeft[r]])
                l += 1
                while l < r and numbersLeft[l] == numbersLeft[l - 1]:
                    l += 1
            elif numbersLeft[l] + numbersLeft[r] < target:
                l += 1
            else:
                r -= 1
        return output

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            if nums[i] > 0:
                break

            pair = self.pair_2sum(nums[i + 1:], -nums[i])
            for p in pair:
                res.append([nums[i]] + p)

        return res