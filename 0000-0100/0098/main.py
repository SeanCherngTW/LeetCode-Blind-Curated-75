class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        if not root:
            return False
        res = self.inorder(root, [])
        for i in range(len(res) - 1):
            if res[i + 1] <= res[i]:
                return False
        return True

    def inorder(self, node, res):
        if not node:
            return res
        res = self.inorder(node.left, res)
        res.append(node.val)
        res = self.inorder(node.right, res)
        return res
