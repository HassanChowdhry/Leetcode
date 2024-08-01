// https://leetcode.com/problems/combination-sum

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        # init variables
        res = []
        can_length = len(candidates)
    
        # inner funct to calc all paths
        def backtrack(inner, total, curr_index):
            if total > target:
                return
            if total == target:
                res.append(inner.copy())
                return

            for i in range(curr_index, can_length):
                num = candidates[i]
                inner.append(num)
                backtrack(inner, total+num, i)
                inner.pop()
        

        
        backtrack([], 0, 0)
        # return
        return res