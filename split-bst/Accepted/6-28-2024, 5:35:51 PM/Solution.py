// https://leetcode.com/problems/split-bst

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def splitBST(self, root: Optional[TreeNode], target: int) -> List[Optional[TreeNode]]:
        
        def dfs(curr):
            if not curr:
                return [None, None]
            
            if curr.val > target:
                left = dfs(curr.left)
                curr.left = left[1]
                return [left[0], curr]
            
            else:
                right = dfs(curr.right)
                curr.right = right[0]
                return [curr, right[1]]

        return dfs(root)
