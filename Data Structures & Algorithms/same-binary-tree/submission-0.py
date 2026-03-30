# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        res1 = []
        res2 = []

        def dfs(node, res):
            if not node:
                res.append(0)
                return
            
            dfs(node.left, res)
            dfs(node.right, res)

            res.append(node.val)

            return

        dfs(p, res1)
        dfs(q, res2)

        return res1 == res2
            