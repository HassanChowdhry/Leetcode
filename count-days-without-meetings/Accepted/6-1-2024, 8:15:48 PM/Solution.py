// https://leetcode.com/problems/count-days-without-meetings

class Solution:
    def countDays(self, days: int, s: List[List[int]]) -> int:
        x = sorted(s, reverse=True, key=lambda x: x[1])
        s.sort()

        def merge():
            stack = []
            stack.append(s[0])

            for i in s[1:]:
                if stack[-1][0] <= i[0] <= stack[-1][-1]:
                    stack[-1][-1] = max(stack[-1][-1], i[-1])
                else:
                    stack.append(i)
            return stack
        
        s = merge()
        
        total = 0
        total += abs(s[0][0] - 1)
        total += abs(x[0][1] - days)

        for i in range(len(s)-1):
            end = s[i][1]
            nxt = s[i+1][0]

            if end > nxt or end == nxt or end+1 == nxt:
                continue
            elif end < nxt:
                total += (abs(nxt - end) - 1)
        
        return total
        
        