// https://leetcode.com/problems/group-anagrams

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mp = {}
        NUM_LETTERS = 26
        # logic - loop, sort word in val append to relevant key
        for word in strs:
            freq = [0] * NUM_LETTERS
            for c in word:
                freq[ord(c)-ord("a")] += 1
            
            freq = tuple(freq)
            if freq in mp:
                mp[freq].append(word)
            else:
                mp[freq] = [word]
        # return
        return mp.values()