// https://leetcode.com/problems/number-of-steps-to-reduce-a-number-in-binary-representation-to-one

class Solution:
    def numSteps(self, s: str) -> int:
        toint = 0

        for c in s:
            toint <<= 1
            toint |= int(c)
        steps = 0

        while toint != 1:
            if toint%2==0:
                toint //= 2
                steps += 1 
            else:
                toint = (toint//2)+1
                steps +=2

        return steps