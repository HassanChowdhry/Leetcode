// https://leetcode.com/problems/merge-triplets-to-form-target-triplet

class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        x=y=z=-1

        for trip in triplets:
            isvalid = True
            for i in range(3):
                if trip[i]>target[i]:
                    isvalid = False
                
            if isvalid:
                x = max(x, trip[0])
                y = max(y, trip[1])
                z = max(z, trip[2])
        

        return x==target[0] and y==target[1] and z==target[2]