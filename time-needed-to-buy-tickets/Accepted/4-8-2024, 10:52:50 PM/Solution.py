// https://leetcode.com/problems/time-needed-to-buy-tickets

class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        ans = 0
        for i in range(len(tickets)):
            if tickets[i] < tickets[k]:
                ans += tickets[i]
            else:
                if i<=k:
                    ans+=tickets[k]
                else:
                    ans+=tickets[k]-1
        return ans