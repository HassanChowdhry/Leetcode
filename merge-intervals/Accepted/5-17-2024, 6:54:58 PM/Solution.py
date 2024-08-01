// https://leetcode.com/problems/merge-intervals

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

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