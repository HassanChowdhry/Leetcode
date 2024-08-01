// https://leetcode.com/problems/the-number-of-beautiful-subsets

class Solution:
    def beautifulSubsets(self, nums: List[int], k: int) -> int:
        def kInArr(arr):
            seen = set()
            for num in arr:
                if num - k in seen or num + k in seen:
                    return True
                seen.add(num)
            return False

        res = []
        n = len(nums)
        nums.sort()

        def backtrack(inner, curr_index):
            if not kInArr(inner):
                res.append(inner.copy())

            for i in range(curr_index, n):
                inner.append(nums[i])
                backtrack(inner, i+1)
                inner.pop()

        backtrack([], 0)
        return len(res)-1