// https://leetcode.com/problems/count-number-of-nice-subarrays

class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        nums = [num % 2 for num in nums]
        queue = 0
        res, gap,start = 0, 0, 0
        print(nums)

        for num in nums:
            if num == 1:
                queue += 1
            if queue == k:
                gap = 0
                while queue == k:
                    if nums[start] == 1:
                        queue -= 1
                    gap += 1
                    start += 1
                
            res += gap

        return res

        
