// https://leetcode.com/problems/remove-element

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        left = 0
        right = len(nums) - 1
        count = 0

        while (left <= right):
          if nums[right] == val:
            right -= 1
            continue
          
          if nums[left] == val:
            nums[left] = nums[right]
            nums[right] = val
            right -= 1
          
          left += 1
          count += 1
        

        return count
