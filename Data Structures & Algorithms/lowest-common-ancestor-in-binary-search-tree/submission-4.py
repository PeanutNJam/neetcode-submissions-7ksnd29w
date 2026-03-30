# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        def dfs(node):
            if not node:
                return None

            left = dfs(node.left)
            right = dfs(node.right)

            if left and right:
                return node

            if (node.val == p.val or node.val == q.val) and (left or right):
                return node

            if (node.val == p.val or node.val == q.val):
                return node

            return left if left else right

        return dfs(root)


