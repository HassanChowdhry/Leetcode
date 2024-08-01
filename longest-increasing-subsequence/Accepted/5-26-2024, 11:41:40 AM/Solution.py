// https://leetcode.com/problems/longest-increasing-subsequence

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:

        # edge case
        if not nums:
            return 0

        # declare
        result = 0
        cache = {}

        # backtrack - logic
        def backtrack(start: int) -> int:

            # base case
            if start == len(nums):
                return 0

            # cache - check
            if start in cache:
                return cache.get(start)

            # recurse
            max_increasing = 1
            for i in range(start+1, len(nums)):
                if nums[i] <= nums[start]:
                    continue
                max_increasing = max(max_increasing, 1 + backtrack(i))

            # cache
            cache[start] = max_increasing

            # return
            return max_increasing

        # backtrack - call
        for start in range(len(nums)):
            result = max(result, backtrack(start))

        # return
        return result