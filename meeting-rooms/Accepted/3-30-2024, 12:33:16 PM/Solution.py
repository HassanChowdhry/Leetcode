// https://leetcode.com/problems/meeting-rooms

class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        intervals.sort(key=lambda x: x[0])
        
        for i in range(1, len(intervals)):
            curr_end = intervals[i-1][1]
            next_start = intervals[i][0]

            if curr_end > next_start:
                return False

        return True