// https://leetcode.com/problems/course-schedule-ii

from collections import deque, defaultdict
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj_map = defaultdict(list)
        pred = [0]*numCourses
        topnum = []
        queue = deque()

        for course, pre in prerequisites:
            pred[course] += 1
            adj_map[pre].append(course)

        for course, pre_count in enumerate(pred):
            if pre_count == 0:
                queue.append(course)
        
        while queue:
            course = queue.popleft()
            topnum.append(course)
            next_course = adj_map[course]
            for c in next_course:
                pred[c]-=1
                if pred[c] == 0:
                    queue.append(c)

        for pre in pred:
            if pre != 0:
                return []

        return topnum