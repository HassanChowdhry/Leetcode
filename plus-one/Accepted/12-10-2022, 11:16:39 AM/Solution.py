// https://leetcode.com/problems/plus-one

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]: 
        str1 = ""
        for digit in digits:
            str1 += str(digit)

        str1 = str(int(str1) + 1)
        
        res = []

        for i in range(len(str1)):
            res.append(int(str1[i]))
        
        return res