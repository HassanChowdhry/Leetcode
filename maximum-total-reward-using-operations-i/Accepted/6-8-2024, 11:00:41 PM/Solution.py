// https://leetcode.com/problems/maximum-total-reward-using-operations-i

class Solution:
    def maxTotalReward(self, rv: List[int]) -> int:
        rv.sort()
        dp, mx = set(),  0
        N = len(rv)
        dp.add(0)
        for i in range(N):
            for j in range(rv[i]-1, -1, -1):
                if j in dp:
                    dp.add(rv[i] + j)
                    mx = max(mx, rv[i] + j)
        
        return mx