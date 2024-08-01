// https://leetcode.com/problems/detect-squares

from collections import defaultdict
class DetectSquares:

    def __init__(self):
        self.graph = defaultdict(int)

    def add(self, point: List[int]) -> None:
        self.graph[tuple(point)] +=1

    def count(self, point: List[int]) -> int:
        take = 0
        x, y = point

        for x2, y2 in self.graph.copy():
            if abs(y-y2) != abs(x-x2) or x==x2 or y==y2 : continue
            
            take += (self.graph[(x2, y2)] * self.graph[(x, y2)] * self.graph[(x2, y)])


        return take

# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)