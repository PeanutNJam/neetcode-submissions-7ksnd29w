# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        def dfs(node):
            if not node:
                return (0, True)
            
            left_count, left_balanced = dfs(node.left)
            right_count, right_balanced = dfs(node.right)

            if left_count < right_count - 1 or right_count < left_count - 1 or not left_balanced or not right_balanced:
                return (max(left_count, right_count) + 1, False)
            
            return (max(left_count, right_count) + 1, True)

        return dfs(root)[1]