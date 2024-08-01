// https://leetcode.com/problems/merge-triplets-to-form-target-triplet

class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        x=y=z=-1

        for t in triplets:
            if x==target[0] and y==target[1] and z==target[2]:
                return True

            if t[0] <= target[0] and t[1] <= target[1] and t[2] <= target[2]:
                x = max(x, t[0])
                y = max(y, t[1])
                z = max(z, t[2])

        return x==target[0] and y==target[1] and z==target[2]