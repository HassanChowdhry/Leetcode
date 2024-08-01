// https://leetcode.com/problems/binary-tree-right-side-view

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # do dfs
        # keep track of level using param, res array appends if not present 
        # traversal goes left then right so last update is rightmost
        res = []
        
        if not root:
            return res
        
        def dfs(root, level):
            if not root:
                return
            
            if level > len(res)-1:
                res.append(root.val)
            else:
                res[level] = root.val
            print(res)
            dfs(root.left, level+1)
            dfs(root.right, level+1)

        


        
        level = 0
        dfs(root, level)
        return res