# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        

        def isValid(left, right, node):
            if not node:
                return True
            
            if node.val <= left or node.val >= right:
                return False

            return isValid(left, node.val, node.left) and isValid(node.val, right, node.right) 

        return isValid(-float("inf"), float("inf"), root)
