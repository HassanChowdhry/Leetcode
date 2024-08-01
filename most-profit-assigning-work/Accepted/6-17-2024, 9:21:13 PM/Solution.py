// https://leetcode.com/problems/most-profit-assigning-work

class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        maxAbility = max(worker)
        jobs = [0] * (maxAbility+1)

        for i in range(len(difficulty)):
            if difficulty[i] > maxAbility: continue
            jobs[difficulty[i]] = max(jobs[difficulty[i]], profit[i])
        
        level_max = 0
        for i in range(len(jobs)):
            level_max = max(level_max, jobs[i])
            jobs[i] = level_max

        total = 0
        for level in worker:
            total += jobs[level]
        return total