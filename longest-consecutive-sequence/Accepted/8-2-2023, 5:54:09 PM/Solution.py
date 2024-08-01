// https://leetcode.com/problems/longest-consecutive-sequence

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
    # declare
        maxRes = 0
        locMax = 1

        # logic – Main loop
        nums.sort()
        for i in range(len(nums) - 1):

            if nums[i + 1] - nums[i] == 1:
                locMax += 1
            elif nums[i + 1] - nums[i] == 0:
                continue
            else :
                maxRes = max(maxRes, locMax)
                locMax =1

        maxRes = max(maxRes, locMax)
        
        # return
        return maxRes