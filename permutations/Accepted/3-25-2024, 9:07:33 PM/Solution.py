// https://leetcode.com/problems/permutations

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # define vars
        res_len = len(nums)
        res = []

        # backtracl: add all leading untill res_len
        def backtrack(inner, curr_index):
            if len(inner) == res_len:
                res.append(inner.copy())
                return
            
            for i in range(curr_index, curr_index+res_len):
                index = i%res_len
                
                if nums[index] in inner:
                    continue

                inner.append(nums[index])
                backtrack(inner, index+1)
                inner.pop()
        
        
        # call func
        backtrack([], 0)
        return res
