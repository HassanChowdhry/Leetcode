// https://leetcode.com/problems/combination-sum

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        # init variables
        res = []
    
        # inner funct to calc all paths
        def backtrack(inner):
            if sum(inner) > target:
                return
            if sum(inner) == target:
                inner.sort()
                if inner not in res:
                    res.append(inner)
                return

            for num in candidates:
                inner.append(num)
                backtrack(inner.copy())
                inner.pop()
        

        
        backtrack([])
        # return
        return res

        