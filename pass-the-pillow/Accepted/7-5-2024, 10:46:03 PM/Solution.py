// https://leetcode.com/problems/pass-the-pillow

class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        start, i = 1, 1
        end = n
        flag = 1
        while time > 0:
            time -=1
            i += flag

            if i == end or i == start:
                flag = -flag

        return i