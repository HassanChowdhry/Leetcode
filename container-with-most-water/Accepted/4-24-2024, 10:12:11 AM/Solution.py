// https://leetcode.com/problems/container-with-most-water

class Solution:
    def maxArea(self, height: List[int]) -> int:
        mxArea = 0
        left = 0
        right = len(height)- 1
        leng = len(height) - 1

        while left < right:
            area = 0
            if (height[left] < height[right]):
                area = height[left] * leng
                left += 1
            
            else:
                area = height[right] * leng
                right -= 1
            
            mxArea = max(mxArea, area)
            leng -= 1
        

        return mxArea