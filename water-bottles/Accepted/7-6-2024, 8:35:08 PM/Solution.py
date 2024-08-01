// https://leetcode.com/problems/water-bottles

class Solution:
    def numWaterBottles(self, bottle: int, ex: int) -> int:
        res = 0
        empty = 0

        while bottle > 0:
            res += bottle
            empty += bottle
            bottle = empty // ex
            empty = empty % ex

        
        return res