// https://leetcode.com/problems/serialize-and-deserialize-binary-tree

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque
class Codec:

    def serialize(self, root):
        ans = []
        empty = "ø"

        def dfs(root):
            if not root:
                ans.append(empty)
                return root
            
            ans.append(str(root.val))
            dfs(root.left)
            dfs(root.right)
            return root

        dfs(root)
        return 'µ'.join(ans)
        

    def deserialize(self, data):
        tree = deque(data.split("µ"))
        root = TreeNode()
        empty = "ø"

        def create(tree):
            if tree[0] == empty:
                tree.popleft()
                return None

            root = TreeNode(tree.popleft())        
            root.left = create(tree)
            root.right= create(tree)

            return root
        return create(tree)

        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))