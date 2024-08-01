// https://leetcode.com/problems/crawler-log-folder

class Solution:
    def minOperations(self, logs: List[str]) -> int:
        res = 0
        for log in logs:
            if log == "../":
                res -= 1
                if res < 0: res = 0
            elif log == "./":
                continue
            else:
                res += 1
        return res