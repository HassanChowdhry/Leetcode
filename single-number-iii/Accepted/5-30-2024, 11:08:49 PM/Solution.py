// https://leetcode.com/problems/single-number-iii

class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        xor = 0

        for num in nums: xor^=num

        diff = 1
        while not(xor & diff):
            diff <<= 1
        
        a = 0

        for num in nums:
            if diff & num:
                a ^= num
        
        return [a, a^xor]