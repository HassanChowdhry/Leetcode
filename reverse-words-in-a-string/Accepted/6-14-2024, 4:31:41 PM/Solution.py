// https://leetcode.com/problems/reverse-words-in-a-string

class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.strip().split(' ')
        s.reverse()
        x = []
        for c in s:
            if c == '':continue
            x.append(c)

        x = ' '.join(x)
        # x = ''.join(s.strip().split(' ').reverse())
        # print(x)
        return x