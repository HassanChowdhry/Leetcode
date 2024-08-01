// https://leetcode.com/problems/binary-tree-maximum-path-sum

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, node: Optional[TreeNode]) -> int:
        res = [float("-inf")]
        def dfs(root):
            if not root:
                return 0

            left = max(dfs(root.left), 0)
            right = max(dfs(root.right), 0)
            
            curr =  root.val + left + right
            res[0] = max(res[0], curr)     
                  
            return max(root.val + left, root.val + right)
        dfs(node)
        return res[0]