// https://leetcode.com/problems/validate-binary-search-tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # just run a inorder, that should be sorted, if not then not valid
            if not root:
                return True
            res = []

            def dfs(root):
                if not root:
                    return True
                
                left = True and dfs(root.left)
                if len(res)>0 and root.val <= res[-1]:
                    return False
                res.append(root.val)

                right = True and dfs(root.right)

                return left and right
            
            return dfs(root)