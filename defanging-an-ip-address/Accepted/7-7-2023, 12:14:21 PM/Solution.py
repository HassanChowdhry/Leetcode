// https://leetcode.com/problems/defanging-an-ip-address

class Solution:
    def defangIPaddr(self, address: str) -> str:
        ans = ''

        for c in address:
            if c == '.':
                ans += '[.]'
            else:
                ans += c
        return ans