// https://leetcode.com/problems/search-in-rotated-sorted-array

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # b search based on range of right and left
        left = 0
        right = len(nums)-1

        while left <= right:
            middle = (left+right)//2
            el = nums[middle]

            if el == target:
                return middle
                
            if el < nums[right]:
                if target > el and target <= nums[right]:
                    left=middle+1
                else:
                    right=middle-1
            else:
                if target > el or target <= nums[right]:
                    left=middle+1
                else:
                    right=middle-1
            
        return -1
