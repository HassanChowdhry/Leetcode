// https://leetcode.com/problems/minimum-difference-between-largest-and-smallest-value-in-three-moves

class Solution:
    def minDifference(self, nums: List[int]) -> int:
        N = len(nums)
        if N <= 4:
            return 0
        nums.sort()
        res = nums[N-1] - nums[0]

        l, r = 2, N

        while l >= -1:
            minn = nums[l+1]
            maxx = nums[r-1]

            res = min(res, maxx-minn)

            l-=1
            r-=1
    
        return res

