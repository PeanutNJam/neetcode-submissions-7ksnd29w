
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from typing import Optional

class Solution:
    def diameterOfBinaryTree(self, root: Optional['TreeNode']) -> int:
        res = 0  # diameter in number of edges

        def dfs(node: Optional['TreeNode']) -> int:
            nonlocal res
            if not node:
                return 0  # height of empty subtree is 0 edges

            left = dfs(node.left)   # height of left subtree
            right = dfs(node.right) # height of right subtree

            # diameter through this node = left height + right height
            res = max(res, left + right)

            # height of this node = 1 + max(left, right)
            return 1 + max(left, right)

        dfs(root)
        return res
