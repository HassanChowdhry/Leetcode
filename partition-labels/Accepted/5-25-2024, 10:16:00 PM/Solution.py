// https://leetcode.com/problems/partition-labels

from collections import defaultdict
class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        intervals = []
        
        n = len(s)
        chars = set(s)
        mp = defaultdict(lambda: [None] * 2)

        for c in chars:
            for i in range(n):
                if s[i]==c:
                    mp[c][0] = i
                    break
            
            for i in range(n-1,-1,-1):
                if s[i]==c:
                    mp[c][1] = i
                    break
        
        for key in mp:
            value = mp[key]
            intervals.append(value)
        
        def merge(intervals: List[List[int]]) -> List[List[int]]:

            intervals = sorted(intervals, key=lambda x: x[0])
            
            res = [intervals[0]]
            i = 0
            j = 1
            n = len(intervals)

            while j<n:
                if res[i][1] < intervals[j][0]:
                    res.append(intervals[j])
                    i+=1
                    j+=1
                    continue
                
                start = res[i][0]
                end = max(res[i][1], intervals[j][1])
                res[i][0] = start
                res[i][1] = end
                j+=1
            
            return res
        
        intervals = merge(intervals)
        return [end+1-start for start, end in intervals]