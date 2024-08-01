// https://leetcode.com/problems/count-good-nodes-in-binary-tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        # dfs: keep track of curr path
        def dfs(curr_node: TreeNode, max_in_path) -> int:
            if not curr_node:
                return 0
            
            good_node = 0

            # add to path, check max vs curr val
            if curr_node.val >= max_in_path:
                good_node = 1
                max_in_path = curr_node.val

            return good_node + dfs(curr_node.left, max_in_path) + dfs(curr_node.right, max_in_path)
        
        return dfs(root, root.val)
        
