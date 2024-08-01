// https://leetcode.com/problems/letter-combinations-of-a-phone-number

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits: return []
        letters = {
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z'],
        }
        res = []
        n = len(digits)

        def backtrack(subset, idx):
            if len(subset) == n:
                string = ''.join(subset)
                res.append(string)
                return
            
            for letter in letters[digits[idx]]:
                subset.append(letter)
                backtrack(subset, idx+1)
                subset.pop()
        
        backtrack([], 0)
        return res