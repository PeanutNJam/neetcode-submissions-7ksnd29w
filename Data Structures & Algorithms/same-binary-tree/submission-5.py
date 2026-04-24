# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        first, second = [], []

        def dfs(node, arr):
            if not node:
                arr.append(None)
                return

            arr.append(node.val) 
            
            dfs(node.left, arr)
            dfs(node.right, arr)

        dfs(p, first)
        dfs(q, second)

        return first == second

        






