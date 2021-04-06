# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        k, res = self.inorder(root, k, None)
        return res

    def inorder(self, node, k, res):
        if not node:
            return k, res
        k, res = self.inorder(node.left, k, res)
        k -= 1
        if k == 0:
            res = node.val
        k, res = self.inorder(node.right, k, res)
        return k, res
