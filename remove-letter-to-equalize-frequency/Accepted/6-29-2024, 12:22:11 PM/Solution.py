// https://leetcode.com/problems/remove-letter-to-equalize-frequency

from collections import defaultdict
class Solution:
    def equalFrequency(self, word: str) -> bool:
        for i in range(len(word)):
            substring = word[:i] + word[i+1:]
            if len(set(Counter(substring).values())) == 1:
                return True

        return False
        
