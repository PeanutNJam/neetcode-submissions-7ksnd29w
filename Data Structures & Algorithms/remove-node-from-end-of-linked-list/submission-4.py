# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head
        curr = dummy

        count_node = head
        count = 0

        while count_node:
            count_node = count_node.next
            count += 1
            
        pos = 1
        count += 1

        while curr:
            if pos != count - n:
                curr = curr.next
                pos += 1
                continue
            
            curr.next = curr.next.next
            curr = curr.next
            pos += 1

        return dummy.next

            
            


            
            
            

