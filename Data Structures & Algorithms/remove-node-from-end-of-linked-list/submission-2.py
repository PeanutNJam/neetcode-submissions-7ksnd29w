# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        prev, curr = None, head
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        count = 1
        curr = prev
        second_prev = None

        while curr:
            if count == n:
                if not curr.next:
                    temp = None
                    curr.next = second_prev
                else:
                    temp = curr.next.next
                    curr.next.next = second_prev
                 
                second_prev = curr.next
                curr = temp
            else:
                temp = curr.next
                curr.next = second_prev
                second_prev = curr
                curr = temp
            count += 1

        return second_prev

        

