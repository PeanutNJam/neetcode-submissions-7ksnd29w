# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        group_prev = dummy

        while True:
            # check if k nodes remain
            kth = group_prev
            for _ in range(k):
                kth = kth.next
                if not kth:
                    return dummy.next

            group_next = kth.next

            # reverse k nodes
            prev, curr = group_next, group_prev.next
            for _ in range(k):
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp

            # reconnect
            temp = group_prev.next
            group_prev.next = prev
            group_prev = temp
