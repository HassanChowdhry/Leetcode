// https://leetcode.com/problems/merge-sorted-array

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        i, j, end = m - 1, n - 1, len(nums1) - 1
    
        while j >= 0:
            if i < 0 or nums1[i] <= nums2[j]:
                nums1[end] = nums2[j]
                j-=1
            else:
                nums1[i], nums1[end] = nums1[end], nums1[i]
                i-=1
            
            end-=1

