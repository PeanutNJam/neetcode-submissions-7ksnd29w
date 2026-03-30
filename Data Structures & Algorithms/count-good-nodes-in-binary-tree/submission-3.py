# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        res = 0

        def dfs(node, curr_max):
            if not node:
                return

            nonlocal res
            if node.val >= curr_max:
                curr_max = node.val
                res += 1

            dfs(node.left, curr_max)
            dfs(node.right, curr_max)

            return

        dfs(root, -101)

        return res
