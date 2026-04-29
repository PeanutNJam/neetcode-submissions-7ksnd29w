"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        node_map = defaultdict(Node)

        curr = head

        while curr:
            node_map[curr] = Node(x=curr.val)
            curr = curr.next

        curr = head
        dummy = Node(x=0)
        curr2 = dummy
        while curr:
            curr2.next = node_map[curr]
            if curr.random:
                curr2.next.random = node_map[curr.random]
            curr2 = curr2.next
            curr = curr.next

        return dummy.next

        
            
