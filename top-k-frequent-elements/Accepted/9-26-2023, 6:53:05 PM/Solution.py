// https://leetcode.com/problems/top-k-frequent-elements

class Solution:
  def topKFrequent(self, nums: list[int], k: int) -> list[int]:
    elMap = {}
    res = []
    
    for num in nums:
      elMap[num] = elMap[num] + 1 if num in elMap else 1
    
    elMap = sorted(elMap.items(), key=lambda x:x[1], reverse=True)
        
    for key in elMap:
      res.append(key[0])
      k -= 1
      if k == 0: break
    
    return res