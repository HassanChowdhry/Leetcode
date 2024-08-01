// https://leetcode.com/problems/most-profit-assigning-work

class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        maxAbility = max(worker)
        jobs = [0] * (maxAbility+1)

        for i in range(len(difficulty)):
            if difficulty[i] <= maxAbility:
                jobs[difficulty[i]] = max(jobs[difficulty[i]], profit[i])
        
        level_max = 0
        for i in range(1, len(jobs)):
            jobs[i] = max(jobs[i], jobs[i - 1])


        total = 0
        for level in worker:
            total += jobs[level]
        return total