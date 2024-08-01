// https://leetcode.com/problems/student-attendance-record-i

import re
class Solution:
    def checkRecord(self, s: str) -> bool:
        return not re.search("A.*A|LLL", s)