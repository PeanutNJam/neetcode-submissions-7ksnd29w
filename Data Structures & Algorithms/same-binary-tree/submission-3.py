# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        q = deque([q])
        p = deque([p])

        while p and q:
            for _ in range(len(p)):
                p_node, q_node = p.popleft(), q.popleft()

                if not p_node and not q_node:
                    continue

                if not p_node or not q_node or p_node.val != q_node.val:
                    return False

                q.append(q_node.left)
                q.append(q_node.right)
                p.append(p_node.left)
                p.append(p_node.right)

        return True
                    
