// https://leetcode.com/problems/multiply-strings

class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if "0" in [num1, num2]:
            return "0"
        N, M = len(num1), len(num2)
        res = [0] * (N+M)
        num1, num2 = num1[::-1], num2[::-1]

        for i in range(N):
            for j in range(M):
                digit = int(num1[i]) * int(num2[j])
                res[i+j] += (digit)
                res[i+j+1] += (res[i+j] // 10)
                res[i+j] = res[i+j] % 10
        
        res = res[::-1]
        start = 0
        while start < (N+M) and res[start] == 0: start+=1 
        res = map(str, res[start:])
        return "".join(res)