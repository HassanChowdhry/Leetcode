// https://leetcode.com/problems/task-scheduler

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = {}

        for task in tasks:
            if task in freq:
                freq[task] += 1
            else:
                freq[task] = 1
        
        max_freq = max(freq.values())
        counter = 0

        for task in freq:
            if freq[task] == max_freq:
                counter +=1

        return max(len(tasks), ((n+1)*(max_freq-1)+counter))
        