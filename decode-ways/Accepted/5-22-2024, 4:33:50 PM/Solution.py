// https://leetcode.com/problems/decode-ways

class Solution:
    def numDecodings(self, s: str) -> int:
        if int(s[0]) == 0:
            return 0
        n = len(s)
        res = [0]*n
        res[0] = 1
        
        def inrange(num):
            if int(num[0]) == 0:
                return False
            return int(num) in range(1, 27)

        for i in range(1, n):
            curr = s[i]
            comb = s[i-1] + s[i]
            if inrange(curr) and inrange(comb):
                res[i] = res[i-1]+(res[i-2] or 1)
            elif inrange(curr) and not inrange(comb):
                res[i] = res[i-1]
            elif not inrange(curr) and inrange(comb):
                res[i] = res[i-2] or 1
            elif not inrange(curr) and not inrange(comb):
                return 0
        print(res)
        return res[-1]