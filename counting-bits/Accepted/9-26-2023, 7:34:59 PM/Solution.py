// https://leetcode.com/problems/counting-bits

class Solution:
    def countBits(self, n: int) -> List[int]:
        res = [0]
        for i in range(1, n + 1):
            sum = 0
            num = i
            while num > 0:
                bit = num % 2
                sum += bit | 0
                num >>= 1
            
            res.append(sum)
        
        return res