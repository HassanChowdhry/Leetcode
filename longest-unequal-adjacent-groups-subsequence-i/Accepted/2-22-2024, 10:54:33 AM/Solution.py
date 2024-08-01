// https://leetcode.com/problems/longest-unequal-adjacent-groups-subsequence-i

class Solution:
    def getLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        # def
        res = []
        prev = -1
        group_len = len(groups)
        
        # main checks what the previous bit was
        for i in range(group_len):
            if prev == groups[i]:
                continue

            res.append(words[i])
            prev = groups[i]

        # return
        return res