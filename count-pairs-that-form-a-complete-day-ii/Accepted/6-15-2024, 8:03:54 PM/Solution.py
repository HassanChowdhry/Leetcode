// https://leetcode.com/problems/count-pairs-that-form-a-complete-day-ii

class Solution:
    def countCompleteDayPairs(self, hours: List[int]) -> int:
        h = [hour % 24 for hour in hours]
        freq = Counter(h)
        res = 0
        
        for curr_hour in freq:
            curr_frq = freq[curr_hour]
            if (curr_hour * 2) % 24 == 0:
                res += ((curr_frq * (curr_frq-1)) // 2)
            
        for i in range(24):
            for j in range(i+1, 24):
                if (i + j) % 24 == 0: 
                    res += (freq[i] * freq[j])
        
        return res