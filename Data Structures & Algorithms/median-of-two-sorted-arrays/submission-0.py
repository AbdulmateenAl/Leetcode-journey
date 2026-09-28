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
    
    def is_a_whole_number(self, num: int) -> bool:
        return num % 1 == 0

    def median(self, nums: List[int]) -> float:
        start = 0
        end = len(nums) - 1

        mid_index = start + ((end - start) / 2)

        if self.is_a_whole_number(mid_index):
            return float(nums[int(mid_index)])
        else:
            left = math.floor(mid_index)
            right = math.ceil(mid_index)

            med = float((nums[left] + nums[right]) / 2)
            return med