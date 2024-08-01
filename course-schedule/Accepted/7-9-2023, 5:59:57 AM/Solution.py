// https://leetcode.com/problems/course-schedule

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
      # contruct map of course to list
      reqMap = {}
      for i in range(numCourses):
        reqMap[i] = []
      
      for course, pre in prerequisites:
        reqMap[course].append(pre)
      
      visited = set()
      def dfs(course):
        if course in visited:
          return False
        if reqMap[course] == []:
            return True

        visited.add(course)
        
        for crs in reqMap[course]:
          if not dfs(crs):
              return False
        visited.remove(course)
        reqMap[course] = []
        return True
        
      for course in reqMap:
        if not dfs(course): return False
      
      return True