// https://leetcode.com/problems/daily-temperatures

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        t_len = len(temperatures)
        res = [0] * t_len
        stack = []
        
        for i in range(t_len):
            val = temperatures[i]

            if len(stack) == 0:
                stack.append((val, i))
                continue
            
            peek = stack[len(stack)-1]

            if val <= peek[0]:
                stack.append((val, i))
                continue
            
            while val > peek[0]:
                top = stack.pop()
                res[top[1]] = (i - top[1])
                
                if len(stack) == 0:
                    break
                peek = stack[len(stack)-1]

            stack.append((val , i))
        return res