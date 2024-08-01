// https://leetcode.com/problems/two-sum

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
      map = {}

      # target 9, nums = [2, 7, 11, 15]
      for i, num in enumerate(nums): # i = 0, 1

        sol = target - nums[i] # 7, 2
        if sol in map:
          return [i, map[sol]]
        else:
          map[nums[i]] = i # {2: 0, }
      
      return []