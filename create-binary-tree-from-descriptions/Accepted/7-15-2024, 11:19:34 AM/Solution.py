// https://leetcode.com/problems/create-binary-tree-from-descriptions

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        mp = {} #val: treenode, isChild

        for parent, child, isLeft in descriptions:
            if parent in mp:
                p = mp[parent][0]
            else:
                p = TreeNode(parent)
            if child in mp:
                c = mp[child][0]
            else:
                c = TreeNode(child)

            if isLeft:
                p.left = c
            else:
                p.right = c

            if parent not in mp:
                mp[parent] = [p, False]
            if child not in mp:
                mp[child] = [c, True]
            mp[child][1] = True
        
        for node in mp:
            if not mp[node][1]:
                return mp[node][0]

        return None