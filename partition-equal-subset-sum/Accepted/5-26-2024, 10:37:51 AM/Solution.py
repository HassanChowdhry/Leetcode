// https://leetcode.com/problems/partition-equal-subset-sum

from collections import defaultdict
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2:
            return False
        dp = defaultdict(set)
        dp[0].add(nums[0])
        
        for i, num in enumerate(nums):
            if i == 0: continue

            children = dp[i-1]
            for child in children:
                sub = child-num
                add = child+num
                if i==len(nums)-1 and (sub == 0 or add == 0):
                    return True

                dp[i].add(sub)
                dp[i].add(add)

        return False

