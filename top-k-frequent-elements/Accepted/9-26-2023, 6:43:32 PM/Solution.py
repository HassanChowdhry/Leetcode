// https://leetcode.com/problems/top-k-frequent-elements

class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        elMap = {}
        res = []
        
        for num in nums:
          elMap[num] = elMap[num] + 1 if num in elMap else 1
        
        while k > 0:
          maxKey = 0
          maxOccur = 0
          
          for key, occur in elMap.items():
            if occur >= maxOccur:
              maxOccur = occur
              maxKey = key
          
          elMap.pop(maxKey)
          res.append(maxKey)
          k-=1
        
        return res