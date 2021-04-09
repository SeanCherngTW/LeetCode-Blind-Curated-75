# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        return self.inorder(s, t)

    def inorder(self, s, t):
        if not s:
            return False
        left_same = self.inorder(s.left, t)
        root_same = self.isSame(s, t)
        right_same = self.inorder(s.right, t)
        return left_same or root_same or right_same

    def isSame(self, s, t):
        if not s and not t:
            return True
        if (not s and t) or (s and not t):
            return False
        return s.val == t.val and self.isSame(s.left, t.left) and self.isSame(s.right, t.right)
