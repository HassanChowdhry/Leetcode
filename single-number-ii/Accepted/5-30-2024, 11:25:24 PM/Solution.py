// https://leetcode.com/problems/single-number-ii

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        freq = Counter(nums)
        for i in freq:
            if freq[i]==1:
                return i
        
        return -1
