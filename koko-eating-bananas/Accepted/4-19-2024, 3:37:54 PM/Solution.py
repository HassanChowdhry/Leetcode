// https://leetcode.com/problems/koko-eating-bananas

class Solution:
    # Time O(nlogn)
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        length = len(piles)
        largest = max(piles)

        # edge cases for effeciency
        if length == 1: return ceil(piles[0]/h)
        if length == h: return largest        

        # helper function to find out if all bananas are consumes
        def is_consumed(k):
            hours = 0
            for num in piles:
                hours += ceil(num/k)

            return hours <= h

        start, end = 1, largest
        min_k = largest

        # binary search to find min k
        while start < end:
            k = ((start + end) // 2)
            is_good = is_consumed(k)

            if is_good:
                min_k = k
                end = k
            else:
                start = k+1

        return min_k