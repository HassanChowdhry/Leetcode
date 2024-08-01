// https://leetcode.com/problems/intersection-of-two-arrays-ii

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        mp = Counter(nums1)
        res = []
        for num in nums2:
            if num in mp:
                mp[num] -= 1
                if mp[num] == 0:
                    del mp[num]
                res.append(num)
    
        return res
