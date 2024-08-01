// https://leetcode.com/problems/daily-temperatures

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        t_len = len(temperatures)
        res = [0] * t_len
        stack = []
        
        for day, temp in enumerate(temperatures):
            while stack and temp > stack[-1][0]:
                top = stack.pop()
                res[top[1]] = (day - top[1])
            
            stack.append((temp , day))
        return res