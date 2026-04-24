# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        q1 = deque([p])
        q2 = deque([q])

        while q1 and q2:
            curr1 = q1.popleft()
            curr2 = q2.popleft()

            if not curr1 and not curr2:
                continue
            if not curr1 or not curr2 or curr1.val != curr2.val:
                return False

            q1.append(curr1.left)
            q1.append(curr1.right)
            q2.append(curr2.left)
            q2.append(curr2.right)

        return True
