# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        res = []

        node_queue = deque([root])
        count = 0

        while node_queue:
            res.append([])
            for _ in range(len(node_queue)):
                curr_node = node_queue.popleft()
                res[count].append(curr_node.val)
                if curr_node.left:
                    node_queue.append(curr_node.left)
                if curr_node.right:
                    node_queue.append(curr_node.right)

            count += 1

        return res


