// https://leetcode.com/problems/minimum-window-substring

from collections import defaultdict
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s): return ""
        l, r = 0, 0
        min_sub = len(s)+1
        ml = mr = -1
        target, curr = Counter(t), defaultdict(int)

        def isSubstring():
            if len(curr) < len(target): return False
            for key in target:
                if target[key] > curr[key]: return False
            return True
        
        while r < len(s):
            if s[r] not in target:
                r+=1
                continue
            curr[s[r]] += 1
            while isSubstring() and l <= r:
                if s[l] in curr:
                    curr[s[l]] -= 1
                    if curr[s[l]] < target[s[l]]:
                        curr[s[l]]+=1
                        if r-l+1 <= min_sub:
                            min_sub = r-l+1
                            mr = r
                            ml = l
                        break
                l+=1
            r+=1

        return "" if min_sub == len(s)+1 else s[ml:mr+1]