// https://leetcode.com/problems/climbing-stairs

class Solution:
    def climbStairs(self, n: int) -> int:
        prev1 = 1
        prev2 = 1

        for i in range(n//2):
            curr1 = prev1+prev2
            curr2 = curr1+prev2

            prev1 = curr1
            prev2 = curr2
        
        return prev1 if n%2==0 else prev2