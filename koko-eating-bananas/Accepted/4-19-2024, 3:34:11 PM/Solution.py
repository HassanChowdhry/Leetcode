// https://leetcode.com/problems/koko-eating-bananas

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        leng = len(piles)
        largest = max(piles)

        if leng == 1: return ceil(piles[0]/h)

        if leng == h: return largest
        # hours = [i+1 for i in range(largest)]
        
        def is_consumed(k):
            hours = 0
            for num in piles:
                hours += ceil(num/k)

            return hours <= h

        start, end = 1, largest
        min_k = largest

        while start < end:
            k = ((start + end) // 2)
            is_good = is_consumed(k)

            if is_good:
                min_k = k
                end = k
            else:
                start = k+1

        return min_k