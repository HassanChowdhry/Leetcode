// https://leetcode.com/problems/special-array-with-x-elements-greater-than-or-equal-x

class Solution:
    def specialArray(self, nums: List[int]) -> int:
        n = len(nums)
        mp = {i:0 for i in range(n+1)}

        for num in nums:
            target = num+1
            if num >= n+1:
                target = n+1
            for i in range(target):
                mp[i] += 1
        
        for i in range(n, -1, -1):
            if i == mp[i]:
                return i
        return -1