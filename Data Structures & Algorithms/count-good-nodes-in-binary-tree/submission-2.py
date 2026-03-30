# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        res = 0
        
        def dfs(node, root_val):
            if not node:
                return

            nonlocal res

            if node.val >= root_val:
                res += 1

            dfs(node.left, max(root_val, node.val))
            dfs(node.right, max(root_val, node.val))

            

        dfs(root, root.val)
        return res
            

            
        