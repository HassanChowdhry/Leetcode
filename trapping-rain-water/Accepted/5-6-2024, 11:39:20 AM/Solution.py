// https://leetcode.com/problems/trapping-rain-water

class Solution:
    def trap(self, height: List[int]) -> int:
        max_right = -1
        max_left = -1

        rain_count = 0

        for i, h in enumerate(height):
            max_left = max(h, max_left)
            max_right = max(height[i:])

            rain_count += min(max_left, max_right) - h
        
        return rain_count
        
