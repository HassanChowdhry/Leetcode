// https://leetcode.com/problems/grumpy-bookstore-owner

class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        res = sum([c if not g else 0 for c, g in zip(customers, grumpy)])

        l, r, curr, add = 0, 0, 0, 0

        for r in range(minutes):
            if grumpy[r]:
                curr += customers[r]
        add = curr
        while r < len(grumpy)-1:
            r+=1
            if grumpy[r]:
                curr += customers[r]
            
            if grumpy[l]:
                curr -= customers[l]
            l+=1
            add = max(add, curr)
            
        return res + add
