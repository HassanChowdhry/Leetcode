// https://leetcode.com/problems/shuffle-the-array

class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        ans = []
        i = 0
        n = len(nums) // 2
        
        while i < n:
            ans.append(nums[i])
            ans.append(nums[i + n])
            i += 1
        
        return ans