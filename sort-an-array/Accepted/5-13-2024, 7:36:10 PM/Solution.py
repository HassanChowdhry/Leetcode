// https://leetcode.com/problems/sort-an-array

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        freq_map = Counter(nums)
        mx = max(nums)
        mn = min(nums)
        idx = 0
        for i in range(mn, mx+1):
            if i not in freq_map:
                continue
            
            frq = freq_map[i]
            for j in range(frq):
                nums[idx] = i
                idx+=1
        return nums