// https://leetcode.com/problems/student-attendance-record-i

class Solution:
    def checkRecord(self, s: str) -> bool:
        absent = 0
        late = 0

        for c in s:
            if c == 'L':
                late += 1
                if late >= 3:
                    return False
                continue
            if c == 'A':
                absent += 1
            late = 0
        
        return absent < 2 and late < 3