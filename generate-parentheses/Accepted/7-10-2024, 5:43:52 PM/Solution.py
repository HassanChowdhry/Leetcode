// https://leetcode.com/problems/generate-parentheses

class Solution(object):
    def generateParenthesis(self, n):
        result = [[""]]

        for i in range(1, n+1):
            current = set()
            for previous in result[i-1]:
                for cut in range(i):
                    first_part = previous[:cut]
                    second_part = previous[cut:]
                    current.add("(" + first_part + ")" + second_part)
            result.append(current)

        return result[n]