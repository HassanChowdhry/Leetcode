// https://leetcode.com/problems/average-waiting-time

class Solution:
    def averageWaitingTime(self, c: List[List[int]]) -> float:
        wait = 0
        end = -1
        n = len(c)
        for start, time in c:
            wait += time
            if start >= end:
                end = start + time
            else:
                wait += (end - start)
                end += time
        
        return wait / n
                
