// https://leetcode.com/problems/set-mismatch

class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        dup, missing = -1, -1
        actual = 0
        for num in nums:
            actual += abs(num)
            if nums[abs(num)-1] < 0:
                dup = num
                continue
            nums[abs(num)-1] *= -1

        N = len(nums)
        expected = ((N * (N+1)) // 2)
        dup = abs(dup)
        return [dup, expected - (actual - dup)]