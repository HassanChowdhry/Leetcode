// https://leetcode.com/problems/partition-labels

class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        mp = {c:i for i,c in enumerate(s)}
        n = len(s)
        res = []
        start = 0
        while start < n:
            end = mp[s[start]]
            i = start
            while i < end:
                i+=1
                end = max(mp[s[i]], end)
            res.append(end+1-start)
            start = i+1
        
        return res

