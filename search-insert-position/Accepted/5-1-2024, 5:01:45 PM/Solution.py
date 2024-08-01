// https://leetcode.com/problems/search-insert-position

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums)-1
        if nums[r] < target:
            return r+1
        elif nums[l] > target:
            return l
            
        while l <= r:
            if l==r:
                return l
            
            mid = (l+r)//2

            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                l = mid+1
            elif nums[mid] > target:
                r = mid
        
        return -1