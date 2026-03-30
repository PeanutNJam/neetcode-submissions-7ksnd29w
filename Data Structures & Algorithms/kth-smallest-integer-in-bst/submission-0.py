# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        curr_list = []
        heapq.heapify(curr_list)

        def dfs(node):
            if not node:
                return

            dfs(node.left)
            dfs(node.right)

            heapq.heappush(curr_list, node.val)


        dfs(root)

        for _ in range(k):
            res = heapq.heappop(curr_list)
        
        return res