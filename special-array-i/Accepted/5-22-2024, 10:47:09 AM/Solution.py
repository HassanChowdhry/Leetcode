// https://leetcode.com/problems/special-array-i

class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        left, right = 0, 1
        n = len(nums)
        if n == 1:
            return True
        
        while left < n and right < n:
            isLeftEven = nums[left]%2
            isRighteven = nums[right]%2

            if isLeftEven == isRighteven:
                return False
            left +=1
            right +=1
        
        return True