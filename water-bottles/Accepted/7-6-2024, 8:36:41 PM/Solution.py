// https://leetcode.com/problems/water-bottles

class Solution:
    def numWaterBottles(self, bottle: int, ex: int) -> int:
        return (bottle * ex - 1) // (ex-1)