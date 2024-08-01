// https://leetcode.com/problems/find-the-town-judge

class Solution:
  def findJudge(self, n: int, trust: list[list[int]]) -> int:
    # edge case
    
    # decalare
    trustMap = { i:[] for i in range(1, n + 1) }
    numOfTrusts = { i:0 for i in range(1, n + 1) }
    
    # the trusted people of a person
    for person, trusts in trust:
      trustMap[person].append(trusts)
    original = trustMap.copy()
      
    visited = set()
    def dfs(person: int):
      if person in visited:
        return
      
      visited.add(person)
      
      for trusts in trustMap[person]:
        dfs(trusts)
        numOfTrusts[trusts] += 1
      visited.remove(person)
      trustMap[person] = []
      
    for person in trustMap:
      dfs(person)
    
    for person, value in numOfTrusts.items():
      if value == n-1 and original[person] == []:
        return person
    # return
    return -1