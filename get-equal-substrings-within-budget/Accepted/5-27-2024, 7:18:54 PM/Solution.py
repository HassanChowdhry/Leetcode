// https://leetcode.com/problems/get-equal-substrings-within-budget

class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        n = len(s)
        cost = [abs(ord(s[i]) - ord(t[i])) for i in range(n)]
        
        l,r = 0,0
        mx, seq, curr = 0,0,0
        while l < n and r < n:
            curr += cost[r]
            if curr <= maxCost:
                mx = max(mx, r-l+1)
                r+=1
                continue
            
            curr -=cost[r]
            curr -=cost[l]
            l+=1
            
        print(cost)
        return mx