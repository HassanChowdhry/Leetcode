// https://leetcode.com/problems/non-overlapping-intervals

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        arr = sorted(intervals, key=lambda x: x[0])
        n = len(intervals)
        if n == 1:
            return 0
        
        left, right = 0, 1
        remove = 0
        while left < n and right < n:
            curr_end = arr[left][1]
            next_start = arr[right][0]

            if curr_end <= next_start:
                left = right
                right +=1
                continue

            remove += 1
            next_end = arr[right][1]
            if curr_end > next_end:
                left = right
            right +=1

        return remove

        