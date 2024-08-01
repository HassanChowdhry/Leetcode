// https://leetcode.com/problems/generate-parentheses

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        sub = []
        def bt(op, cl):          
            if op > n or cl > n:
                return
                
            if op == n and cl == n:
                res.append(''.join(sub))
                return
            
            if op >= cl:
                sub.append("(")
                bt(op+1, cl)
                sub.pop()
            
            if cl <= n:
                sub.append(")")
                bt(op, cl+1)
                sub.pop()
            
        bt(0, 0)
        return res