# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        node_map = defaultdict(list)
        q = deque([[root, 0]])

        while q:
            node, count = q.popleft()

            node_map[count].append(node.val)

            if node.left:
                q.append([node.left, count + 1])
            if node.right:
                q.append([node.right, count + 1])

        res = []

        for val in node_map.values():
            res.append(val[-1])

        return res

