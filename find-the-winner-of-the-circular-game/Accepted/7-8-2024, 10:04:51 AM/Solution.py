// https://leetcode.com/problems/find-the-winner-of-the-circular-game

class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        res = [i for i in range(1, n+1)]

        curr = 0
        while len(res) > 1:
            curr += (k-1)
            curr = curr % len(res)
            del res[curr]
        
        return res[0]
