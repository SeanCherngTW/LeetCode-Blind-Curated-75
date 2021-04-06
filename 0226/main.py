# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTreeDFS(self, root: TreeNode) -> TreeNode:
        return self.invert(root)

    def invert(self, node):
        if not node:
            return None
        else:
            left = node.left
            right = node.right
            node.left = self.invert(right)
            node.right = self.invert(left)
        return node

    def invertTreeBFS(self, root: TreeNode) -> TreeNode:
        if not root:
            return None

        queue = []
        queue.append(root)

        while queue:
            node = queue.pop()
            node.left, node.right = node.right, node.left
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        return root
