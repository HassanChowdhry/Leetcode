// https://leetcode.com/problems/pass-the-pillow

class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        mod = (n-1)*2

        res = time % mod

        return n - abs(res - n + 1)