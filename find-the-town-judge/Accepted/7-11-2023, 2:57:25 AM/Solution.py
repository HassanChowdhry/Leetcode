// https://leetcode.com/problems/find-the-town-judge

class Solution:
  def findJudge(self, n: int, trust: list[list[int]]) -> int:
    numOfTrusted = { i:0 for i in range(1, n + 1) }
    for person, trusts in trust:
      numOfTrusted[person] -= 1
      numOfTrusted[trusts] += 1
    
    for person, trusted in numOfTrusted.items():
      if trusted == n-1:
        return person
    
    return -1