# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = -float("inf")

        def dfs(root):
            if not root:
                return
            
            nonlocal res

            left = maxVal(root.left)
            right = maxVal(root.right)

            res = max(res, left + right + root.val)

            dfs(root.left)
            dfs(root.right)

        def maxVal(root):
            if not root:
                return 0

            left = maxVal(root.left)
            right = maxVal(root.right)

            val = root.val + max(left, right)
            return max(0, val)

        dfs(root)
        return res