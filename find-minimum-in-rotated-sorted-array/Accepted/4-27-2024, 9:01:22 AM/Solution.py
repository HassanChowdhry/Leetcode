// https://leetcode.com/problems/find-minimum-in-rotated-sorted-array

class Solution:
    def findMin(self, nums: List[int]) -> int:
        res = float("inf")
        
        left = 0
        right = len(nums)-1

        while left <= right:
            middle = (left+right)//2
            curr = nums[middle]

            res = min(res, curr)

            if curr > nums[right]:
                left=middle+1
            else:
                right=middle-1
        
        return res