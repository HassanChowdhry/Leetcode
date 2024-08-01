// https://leetcode.com/problems/delete-nodes-and-return-forest

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        td = set(to_delete)
        res = []

        def dfs(root: TreeNode) -> None:
            if not root:
                return None
            
            root.left = dfs(root.left)
            root.right = dfs(root.right)

            if root.val in td:
                if root.left:
                    res.append(root.left)
                if root.right:
                    res.append(root.right)
                return None
            return root
        
        root = dfs(root)
        if root and root not in td: res.append(root)
        return res