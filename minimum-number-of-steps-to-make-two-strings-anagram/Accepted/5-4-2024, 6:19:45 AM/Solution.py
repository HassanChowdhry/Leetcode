// https://leetcode.com/problems/minimum-number-of-steps-to-make-two-strings-anagram

class Solution:
    def minSteps(self, s: str, t: str) -> int:
        pair1 = {}
        pair2 = {}
        count = 0

        for c in s:
            if c in pair1:
                pair1[c] += 1
            else:
                pair1[c] = 1

        for c in t:
            if c in pair2:
                pair2[c] += 1
            else:
                pair2[c] = 1

        for key in pair1:
            if key in pair2:
                curr = pair1[key]-pair2[key]
                if curr < 0: curr = 0
                count += curr
            else:
                count += pair1[key]
        return count