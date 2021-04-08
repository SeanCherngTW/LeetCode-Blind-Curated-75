# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        return self.length(root, 1)

    def length(self, node, cur_len):
        if not node:
            return cur_len - 1
        return max(self.length(node.left, cur_len + 1), self.length(node.right, cur_len + 1))
