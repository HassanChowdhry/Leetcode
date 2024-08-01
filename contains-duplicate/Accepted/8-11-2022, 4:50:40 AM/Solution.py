// https://leetcode.com/problems/contains-duplicate

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hash_set = set()
        for i, num in enumerate(nums):
            if num in hash_set:
                return True
            else: 
                hash_set.add(num)
        return False