// https://leetcode.com/problems/insert-interval

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        s, e = newInterval

        if len(intervals) == 0:
            return [newInterval]

        for i, interval in enumerate(intervals):
            start, end = interval

            if len(res)==0 and start>e:
                res.append(newInterval)
                res.append(interval)
                continue
            
            if s>intervals[i-1][0] and e<start:
                res.append(newInterval)

            if s>end or start>e: 
                res.append(interval)
                continue
            
            s = min(s, start)
            e = max(e, end)
            if len(res)>0 and res[-1][0] == s:
                res[-1][0] = s
                res[-1][1] = e
            else:
                res.append([s, e])

        if newInterval[0] > res[-1][1]:
            res.append(newInterval)
        return res
            