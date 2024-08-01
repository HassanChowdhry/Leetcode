// https://leetcode.com/problems/group-anagrams

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagramMap = {}
        res = []
        
        # logic
        for str in strs:
            sortedStr = ''.join(sorted(str))
            if sortedStr in anagramMap:
                anagramMap[sortedStr].append(str)
            else:
                anagramMap[sortedStr] = [str]
            
        # logic
        return [value for value in anagramMap.values()]