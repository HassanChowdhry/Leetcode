// https://leetcode.com/problems/sort-colors

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        freq_map = Counter(nums)
        print(freq_map)

        idx = 0
        for i in range(3):
            if i not in freq_map:
                continue
            
            frq = freq_map[i]
            for j in range(frq):
                nums[idx] = i
                idx+=1