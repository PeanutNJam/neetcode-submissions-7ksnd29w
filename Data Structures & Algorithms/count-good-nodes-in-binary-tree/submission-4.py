# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0

        res = 0

        def dfs(node, val):
            if not node:
                return

            nonlocal res

            if node.val >= val:
                val = node.val
                res += 1

            dfs(node.left, val)
            dfs(node.right, val)

        dfs(root, -101)

        return res







            