// https://leetcode.com/problems/clone-graph

# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class Solution:
    def cloneGraph(self, node: Node) -> Node:
      if not node:
        return None
      
      visited = {}
      
      def bfs() -> Node:
        queue = deque()
        queue.append(node)
        
        while queue:
          curr:Node = queue.popleft()
                    
          if curr in visited:
            clone = visited[curr]
          else:
            clone = Node(curr.val)
            visited[curr] = clone
        
          
          for edge in curr.neighbors:
            if edge in visited:
              clone.neighbors.append(visited[edge])
            else:
              value = Node(edge.val)
              visited[edge] = value
              clone.neighbors.append(value)
              queue.append(edge)
            
        return visited[node]
      
      return bfs()