// https://leetcode.com/problems/find-the-n-th-value-after-k-seconds

class Solution:
    def valueAfterKSeconds(self, n: int, k: int) -> int:
        MOD = 10**9 + 7
        res = [1] * n

        for i in range(k):
            prefix = 0
            for j in range(n):
                prefix = ((prefix + res[j]) % MOD)
                res[j] = prefix
        
        # print(res)
        return res[-1]