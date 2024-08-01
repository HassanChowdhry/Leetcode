// https://leetcode.com/problems/clone-graph

"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
      if not node:
        return None
      
      visited = {}
      return self.dfs(node, visited)
    
    def dfs(self, node: 'Node', visited: set):
      if node in visited:
        return visited[node]
      
      clone = Node(node.val)
      visited[node] = clone
      
      for edge in node.neighbors:
        clone.neighbors.append(self.dfs(edge, visited))
          
      return clone