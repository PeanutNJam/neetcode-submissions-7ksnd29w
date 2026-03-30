# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        def dfs(node, count):
            if not node:
                return count

            left_count = right_count = count

            if node.left:
                left_count = max(left_count, dfs(node.left, count + 1))
            if node.right:
                right_count = max(right_count, dfs(node.right, count + 1))

            return max(left_count, right_count)

        return dfs(root, 1)
            