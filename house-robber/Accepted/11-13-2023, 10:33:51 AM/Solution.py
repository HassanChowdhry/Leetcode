// https://leetcode.com/problems/house-robber

class Solution:
    def rob(self, nums: List[int]) -> int:
      memo = {}
      def fibb(index):
        if index >= len(nums):
          return 0
        
        if index not in memo:
          memo[index] = nums[index] + max(fibb(index + 2), fibb(index + 3))

        return memo[index]

      return max(fibb(0), fibb(1))