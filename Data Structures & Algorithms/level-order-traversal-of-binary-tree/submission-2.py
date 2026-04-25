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
        count_map = defaultdict(list)

        count = 0

        q = deque([[root, 0]])

        while q:
            node, count = q.popleft()
            count_map[count].append(node.val)

            if node.left:
                q.append([node.left, count + 1])
            if node.right:
                q.append([node.right, count + 1])

        for val in count_map.values():
            res.append(val)

        return res

        