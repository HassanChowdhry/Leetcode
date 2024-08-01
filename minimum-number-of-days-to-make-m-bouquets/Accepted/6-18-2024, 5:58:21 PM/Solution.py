// https://leetcode.com/problems/minimum-number-of-days-to-make-m-bouquets

class Solution:
    def minDays(self, bd: List[int], m: int, k: int) -> int:
        low, high = min(bd), max(bd)
        N = len(bd)
        ans = -1
        while low <= high:
            mid = (low + high) // 2

            res, curr_bouq = 0, 0
            for day in bd:
                if day <= mid:
                    curr_bouq += 1
                else:
                    curr_bouq = 0
                
                if curr_bouq >= k:
                    res +=1
                    curr_bouq = 0

            if res >= m:
                ans = mid
                high = mid-1
            elif res < m:
                low = mid +1

        return ans

