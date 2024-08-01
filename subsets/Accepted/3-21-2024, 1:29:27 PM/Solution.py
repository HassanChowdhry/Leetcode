// https://leetcode.com/problems/subsets

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # init variables
        res = []
        
        # run an array adding a num, then calling func, then popping that num
        def backtrack(inner, curr_index, list_len):
            res.append(inner)

            for i in range(curr_index, list_len):
                inner.append(nums[i])
                backtrack(inner.copy(), i+1, list_len)
                inner.pop()

        backtrack([], 0, len(nums))
        return res