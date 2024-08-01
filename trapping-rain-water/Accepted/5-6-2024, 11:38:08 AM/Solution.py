// https://leetcode.com/problems/trapping-rain-water

class Solution:
    def trap(self, height: List[int]) -> int:
        # maxr = -1
        # maxidx = -1
        # for i, h in enumerate(height):
        #     if h >= maxr:
        #         maxr = h
        #         maxidx = i
        
        # max_map = {}


        # for i, h in enumerate(height):
            
        
        # return rain

        # declare
        max_right = -1
        max_left = -1

        rain_count = 0

        for i, h in enumerate(height):
            max_left = max(height[:i+1])
            max_right = max(height[i:])

            rain_count += min(max_left, max_right) - h
            print(f'curr: {h}, left: {max_left}, right: {max_right}')
        
        return rain_count
        
