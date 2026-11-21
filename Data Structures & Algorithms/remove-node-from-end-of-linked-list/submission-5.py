# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        counter = head
        total = 0
        while counter:
            total += 1
            counter = counter.next

        count = 1
        dummy = ListNode(val=-1)
        dummy.next = head
        prev, curr = dummy, head


        while curr:
            if total - count + 1 == n:
                prev.next = curr.next
            else:
                prev = curr
            curr = curr.next
            count += 1

        return dummy.next


        
        