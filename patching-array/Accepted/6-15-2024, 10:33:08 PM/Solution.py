// https://leetcode.com/problems/patching-array

class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        miss = 1
        i = patches = 0


        while miss <= n:
            if i < len(nums) and miss >= nums[i]:
                miss += nums[i]
                i+=1
            else:
                miss += miss
                patches += 1
        
        return patches
        