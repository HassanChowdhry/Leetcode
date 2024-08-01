// https://leetcode.com/problems/largest-positive-integer-that-exists-with-its-negative

class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        nset = set()
        res = -1
        for num in nums:
            if (-num) in nset:
                res = max(abs(num), res)
            else:
                nset.add(num)
        return res