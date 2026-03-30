# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        if not root:
            return "N"
        
        res = []
        queue = deque([root])
        while queue:
            curr = queue.popleft()
            if curr:
                res.append(str(curr.val))
                queue.append(curr.left)
                queue.append(curr.right)
            else:
                res.append("N")

        return ",".join(res)

        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        val = data.split(",")

        if val[0] == "N":
            return None

        root = TreeNode(val=int(val[0]))
        queue = deque([root])
        index = 1
        while queue:
            curr = queue.popleft()

            if val[index] != "N":
                curr.left = TreeNode(int(val[index]))
                queue.append(curr.left)
            index += 1

            if val[index] != "N":
                curr.right = TreeNode(int(val[index]))
                queue.append(curr.right)
            index += 1

        return root



        



