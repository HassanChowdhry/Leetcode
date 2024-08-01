// https://leetcode.com/problems/roman-to-integer


  
#   for (let i = 0; i < s.length; i++) {
#     let currentRoman = romanMap.get(s[i]);
#     let nextRoman = romanMap.get(s[i + 1]);
    
#     if (currentRoman < nextRoman) {
#       num -= currentRoman;
#     } else {
#       num += currentRoman;
#     }
#   }

#   return num;
class Solution:
    def romanToInt(self, s: str) -> int:
        rom = {
            'M': 1000,
            'D': 500,
            'C': 100,
            'L': 50,
            'X': 10,
            'V': 5,
            'I': 1
        }
        res = 0

        for i in range(len(s)):
            curr = rom[s[i]]

            if i == len(s)-1:
                res += curr
                continue
            next = rom[s[i+1]]

            if curr < next:
                res -= curr
            else:
                res += curr
        
        return res