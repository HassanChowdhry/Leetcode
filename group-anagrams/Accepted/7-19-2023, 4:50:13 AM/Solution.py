// https://leetcode.com/problems/group-anagrams

# https://leetcode.com/problems/group-anagrams/

class Solution(object):
    # Time O(nmlogm), Space O(n)
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
      # declare
      anagramMap = {}
      
      # appends to a key that is sorted version of anagram
      for str in strs:
        sortedStr = ''.join(sorted(str))
        if sortedStr in anagramMap:
          anagramMap[sortedStr].append(str)
        else:
          anagramMap[sortedStr] = [str]
        
      # return all arrays in map
      return anagramMap.values()