// https://leetcode.com/problems/longest-consecutive-sequence

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # try using hashmap
        if not nums:
            return 0
        # declare
        store = {num: 1 for num in nums}
        
        # logic - key will be number and value will be number of instances
        
        for num in list(store.keys()):
            check = num + 1
            while check in store:
                store[num] += store[check]
                del store[check]
                check += 1
        
        # return
        return max(store.values())