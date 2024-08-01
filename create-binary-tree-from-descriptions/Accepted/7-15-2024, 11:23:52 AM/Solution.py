// https://leetcode.com/problems/create-binary-tree-from-descriptions

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import defaultdict
class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        mp = defaultdict() #val: treenode, isChild
        children = set()

        for parent, child, isLeft in descriptions:
            if parent not in mp:
                mp[parent] = TreeNode(parent)
            if child not in mp:
                mp[child] = TreeNode(child)

            if isLeft:
                mp[parent].left = mp[child]
            else:
                mp[parent].right = mp[child]

            children.add(child)
        
        for node in mp:
            if node not in children:
                return mp[node]