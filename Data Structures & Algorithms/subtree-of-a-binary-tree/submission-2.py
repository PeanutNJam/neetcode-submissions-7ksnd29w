# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        res = False
        
        def dfs(node):
            if not node:
                return

            dfs(node.left)
            dfs(node.right)

            if node.val == subRoot.val:
                nonlocal res
                q1, q2 = deque([node]), deque([subRoot])

                while q1 and q2:
                    curr1 = q1.popleft()
                    curr2 = q2.popleft()
                    if not curr1 and not curr2:
                        continue
                    
                    if not curr1 or not curr2 or curr1.val != curr2.val:
                        return
                    q1.append(curr1.left)
                    q1.append(curr1.right)
                    q2.append(curr2.left)
                    q2.append(curr2.right)

                res = True

        dfs(root)

        return res

