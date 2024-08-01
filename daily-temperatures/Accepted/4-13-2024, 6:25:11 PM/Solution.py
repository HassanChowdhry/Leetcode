// https://leetcode.com/problems/daily-temperatures

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        t_len = len(temperatures)
        res = [0] * t_len
        stack = []
        
        for day, temp in enumerate(temperatures):

            if len(stack) == 0:
                stack.append((temp, day))
                continue
            
            peek = stack[len(stack)-1]
            
            while stack and temp > peek[0]:
                top = stack.pop()
                res[top[1]] = (day - top[1])
                
                if len(stack) == 0:
                    break
                peek = stack[len(stack)-1]

            stack.append((temp , day))
        return res