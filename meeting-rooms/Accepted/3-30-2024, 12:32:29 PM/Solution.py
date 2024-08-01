// https://leetcode.com/problems/meeting-rooms

class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        intervals.sort(key=lambda x: x[0])
        

        for i in range(1, len(intervals)):
            start_1 = intervals[i-1][0]
            end_1 = intervals[i-1][1]
            
            start_2 = intervals[i][0]
            end_2 = intervals[i][1]

            if end_1 > start_2:
                return False


        return True