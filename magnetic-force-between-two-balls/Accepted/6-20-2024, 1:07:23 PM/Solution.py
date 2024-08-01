// https://leetcode.com/problems/magnetic-force-between-two-balls

class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        p = sorted(position)
        if m == 2:
            return p[-1] - p[0]

        left, right = 0, ceil(p[-1]/(m-1))
        
        force = 0
        while left <= right:
            mid = (left + right) // 2

            res, balls = 0, 1
            prev = p[0]
            for num in p[1:]:
                res += (num - prev)
                prev = num
                if res >= mid:
                    res = 0
                    balls += 1
                if balls == m:
                    break
            if balls == m:
                force = mid
                left = mid+1
            else:
                right = mid-1
        
        return force
        