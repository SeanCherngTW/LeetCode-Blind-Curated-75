class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []

        queue = [root]
        res = [[root.val]]

        while queue:
            level = []
            for node in queue:
                if node.left:
                    level.append(node.left)
                if node.right:
                    level.append(node.right)
            queue = level

            if level != []:
                res.append([node.val for node in level])

        return res

    def levelOrderV2(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []

        queue = [root]
        res = [[root.val]]

        while queue:
            level = []
            for node in queue:
                if node.left:
                    level.append(node.left)
                if node.right:
                    level.append(node.right)
            queue = level

            if level != []:
                res.append([node.val for node in level])

        return res
