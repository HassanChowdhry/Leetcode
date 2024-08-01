// https://leetcode.com/problems/course-schedule

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
      # inits maps
      courses = {i:[] for i in range(numCourses)}
      isNotLoop = True
      
      for pre, course in prerequisites:
        courses[pre].append(course)
      
      def dfs(pre, visited):
        isNotLooped = True
        if len(courses[pre]) == 0:
          return True
        
        if pre in visited:
          return False
        
        visited.add(pre)
        for course in courses[pre]:
          isNotLooped &= dfs(course, visited)
          courses[course] = []
        
          
        return isNotLooped
      
      # main process
      for pre in courses:
        visited = set()
        isNotLoop &= dfs(pre, visited)
        courses[pre] = []
        
      # end
      return isNotLoop