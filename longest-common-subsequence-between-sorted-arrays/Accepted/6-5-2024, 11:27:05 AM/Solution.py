// https://leetcode.com/problems/longest-common-subsequence-between-sorted-arrays

from collections import defaultdict
from typing import List
class Solution:
    def longestCommonSubsequence(self, arrays: List[List[int]]) -> List[int]:
        count = defaultdict(int)
        array_count = len(arrays)

        for array in arrays:
            for num in array:
                count[num] += 1
        
        res = []
        for key in count:
            if count[key] == array_count:
                res.append(key)
        return res

