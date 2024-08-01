// https://leetcode.com/problems/group-anagrams

class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        # declare
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