// https://leetcode.com/problems/permutation-in-string

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # throw s1 into set
        # use slider to find any occurence of s1, dynamically adjust left side according to repitition
        smap = {}
        for char in s1:
            if char in smap:
                smap[char]+=1
            else:
                smap[char]=1
        
        res = {}
        l = r = 0

        for i, char in enumerate(s2):
            if res == smap: return True
            
            if char not in smap:
                l = r = (i+1)
                res = {}
                continue
            
            r=i

            if char not in res:
                res[char] = 1
                continue
            
            res[char]+=1
            if smap[char] < res[char]:
                temp = l
                while (smap[char] != res[char]) and l<=r:
                    c = s2[l]
                    res[c] -= 1
                    if res[c] == 0:
                        del res[c]
                    l+=1
        
        return res == smap

