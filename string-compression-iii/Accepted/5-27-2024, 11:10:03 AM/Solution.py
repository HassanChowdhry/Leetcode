// https://leetcode.com/problems/string-compression-iii

class Solution:
    def compressedString(self, word: str) -> str:
        res = ""
        n = len(word)

        left, right = 0,1

        while left < n and right <= n:
            prefix = right-left

            if right<n and word[left] == word[right] and prefix < 9:
                right +=1
                continue
            
            res += str(prefix)
            res += word[left]
            left = right
            right +=1
        
        return res