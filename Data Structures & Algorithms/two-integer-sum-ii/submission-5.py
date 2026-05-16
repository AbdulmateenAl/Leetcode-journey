class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # Using binary search
        for i in range(len(numbers)):
            l, r = i + 1, len(numbers) - 1
            res = target - numbers[i]
            while l <= r:
                mid = (l + r) // 2
                if res == numbers[mid]:
                    return [i + 1, mid + 1]
                elif res < numbers[mid]:
                    r = mid - 1
                else:
                    l = mid + 1