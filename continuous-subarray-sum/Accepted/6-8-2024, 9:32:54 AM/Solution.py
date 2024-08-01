// https://leetcode.com/problems/continuous-subarray-sum

class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        if len(nums) == 1:
            return False
        seen = {0: -1}
        running = 0

        for i, num in enumerate(nums):
            running += num
            mod = running % k
            if mod in seen:
                if i - seen[mod] > 1:
                    return True
            else:
                seen[mod] = i
        
        return False
            