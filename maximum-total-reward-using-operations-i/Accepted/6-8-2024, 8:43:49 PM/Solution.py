// https://leetcode.com/problems/maximum-total-reward-using-operations-i

class Solution:
    def maxTotalReward(self, rv: List[int]) -> int:
        rv.sort()
        dp = {}
        N = len(rv)
        dp[0] = 1
        for i in range(N):
            for j in range(rv[i]-1, -1, -1):
                if j in dp:
                    dp[rv[i] + j] = 1
        
        res = 0
        for key in dp:
            res = max(res, key)
        
        return res