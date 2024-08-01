// https://leetcode.com/problems/trapping-rain-water

class Solution:
    def trap(self, height: List[int]) -> int:
        max_left = -1
        max_left_idx = -1
        max_right = max(height)
        rain_count = 0
        for i, h in enumerate(height):
            max_left = max(h, max_left)
            if max_left == max_right:
                max_left_idx = i
                break

            rain_count += min(max_left, max_right) - h
            
        max_right = -1
        for i in range(len(height)-1, max_left_idx, -1):
            h = height[i]
            max_right = max(max_right, h)

            rain_count += min(max_left, max_right) - h
        
        return rain_count
        
