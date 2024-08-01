// https://leetcode.com/problems/remove-vowels-from-a-string

class Solution:
    def removeVowels(self, s: str) -> str:
        sets = set(('a', 'i', 'e', 'o', 'u'))
        ans = ''

        for c in s:
            if c not in sets:
                ans += c
        
        return ans