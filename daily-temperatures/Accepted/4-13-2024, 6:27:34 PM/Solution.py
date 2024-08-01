// https://leetcode.com/problems/daily-temperatures

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        t_len = len(temperatures)
        res = [0] * t_len
        stack = []
        
        for day, temp in enumerate(temperatures):
            
            while stack and temp > temperatures[stack[-1]]:
                top = stack.pop()
                res[top] = day - top

            stack.append(day)
        return res