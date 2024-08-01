// https://leetcode.com/problems/partition-equal-subset-sum

from collections import defaultdict
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2:
            return False
        dp = set()
        dp.add(0)
        target = (total//2)
        
        for i in range(len(nums)-1, -1, -1):
            num = nums[i]
            if num == target:
                return True

            for child in dp.copy():
                add = child+num
                if add == target:
                    return True
                dp.add(add)

        return False

