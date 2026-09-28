class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        i = j = 0
        merged_arr = []

        while i < len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]:
                merged_arr.append(nums1[i])
                i += 1
            else:
                merged_arr.append(nums2[j])
                j += 1

        while i < len(nums1):
            merged_arr.append(nums1[i])
            i += 1

        while j < len(nums2):
            merged_arr.append(nums2[j])
            j += 1

        res = self.median(merged_arr)

        return res

    def median(self, nums: List[int]) -> float:
        totalLen = len(nums)

        if totalLen % 2 == 0:
            return (nums[(totalLen // 2) - 1] + nums[totalLen // 2]) / 2.0
        else:
            return nums[totalLen // 2]