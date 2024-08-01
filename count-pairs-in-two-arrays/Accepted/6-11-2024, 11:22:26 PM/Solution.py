// https://leetcode.com/problems/count-pairs-in-two-arrays

class Solution:
    def countPairs(self, nums1: List[int], nums2: List[int]) -> int:
        N = len(nums1)

        diff = sorted([n1 - n2 for n1, n2 in zip(nums1, nums2)])

        l, r = 0, N-1

        res = 0
        while l < r:
            if (diff[l] + diff[r]) > 0:
                res += (r-l)
                r-=1
            else:
                l+=1
        return res



