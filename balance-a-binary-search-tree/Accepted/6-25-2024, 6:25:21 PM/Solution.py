// https://leetcode.com/problems/balance-a-binary-search-tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        nums = []
        def dfs(root):
            if not root: return
            dfs(root.left)
            nums.append(root.val)
            dfs(root.right)
        dfs(root)

        if len(nums)<=2:
            return root
        
        def createBST(root, l, r):
            if l > r:
                return None
            mid = (r + l) // 2
            
            root = TreeNode(nums[mid])
            root.left = createBST(None, l, mid-1)
            root.right = createBST(None, mid+1, r)

            return root
        
        r = len(nums)-1
        l = 0
        new_root = createBST(None, l, r)
        return new_root

