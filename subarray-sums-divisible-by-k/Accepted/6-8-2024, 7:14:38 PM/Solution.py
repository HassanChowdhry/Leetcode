// https://leetcode.com/problems/subarray-sums-divisible-by-k

from collections import defaultdict
class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        seen = defaultdict(int)
        prefix = 0

        for num in nums:
            prefix += num
            mod = prefix % k
            seen[mod] += 1

        res = 0
        for key in seen:
            val = seen[key]
            if key == 0:
                res += ((val * (val+1)) // 2)
            else:
                res += ((val * (val-1)) // 2)
        return res