// https://leetcode.com/problems/count-pairs-that-form-a-complete-day-i

class Solution:
    def countCompleteDayPairs(self, hours: List[int]) -> int:
        res = 0
        N = len(hours)

        for i in range(N):
            for j in range(i+1, N):
                if (hours[i] + hours[j]) % 24 == 0:
                    res += 1
        
        return res