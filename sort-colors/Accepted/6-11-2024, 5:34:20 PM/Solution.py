// https://leetcode.com/problems/sort-colors

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        freq = Counter(nums)

        i = 0
        for num in range(3):
            val = freq[num]
            for j in range(val):
                nums[i] = num
                i+=1