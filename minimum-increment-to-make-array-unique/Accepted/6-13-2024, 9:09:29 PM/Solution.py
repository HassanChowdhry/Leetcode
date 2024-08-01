// https://leetcode.com/problems/minimum-increment-to-make-array-unique

class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        nums.sort()

        res = 0

        for i in range(1, len(nums)):
            num = nums[i]
            if num <= nums[i-1]:
                res += abs(nums[i-1] - num) + 1
                nums[i] = nums[i-1] + 1
            
        return res