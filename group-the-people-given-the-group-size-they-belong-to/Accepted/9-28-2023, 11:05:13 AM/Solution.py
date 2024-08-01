// https://leetcode.com/problems/group-the-people-given-the-group-size-they-belong-to

class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        res = []
        countMap = dict()

        for i, val in enumerate(groupSizes):
            if val in countMap:
                countMap[val].append(i)
            else:
                countMap[val] = [i]
                        
            if (len(countMap[val]) == val):
                res.append(countMap.pop(val))            
        
        return res
