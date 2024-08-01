// https://leetcode.com/problems/average-waiting-time

class Solution:
    def averageWaitingTime(self, c: List[List[int]]) -> float:
        wait = 0
        end = -1
        for start, time in c:
            wait += time
            if start >= end:
                end = start + time
            else:
                wait += (end - start)
                end += time
        
        return wait / len(c)
                
