// https://leetcode.com/problems/k-closest-points-to-origin

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distances = []

        i = 0
        for point in points:
            x, y = point
            dist = x**2 + y**2
            distances.append((dist, i))
            i+=1

        distances = sorted(distances, key=lambda x: x[0])

        res = []
        j = 0
        for dist, i in distances:
            if j == k: break
            res.append(points[i])
            j+=1
        return res