class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def same_node(node1, node2):
            if not node1 and not node2:
                return True
            if not node1 or not node2:
                return False
            if node1.val != node2.val:
                return False

            return same_node(node1.left, node2.left) and same_node(node1.right, node2.right)


        def dfs(node):
            if not node:
                return False

            if same_node(node, subRoot):
                return True

            return dfs(node.left) or dfs(node.right)

            
        return dfs(root)

