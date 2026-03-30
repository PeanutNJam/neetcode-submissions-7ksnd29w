# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        curr, prev = l1, None
        square = -1
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
            square += 1
        
        res1 = 0
        while prev:
            res1 += prev.val * 10**square
            square -= 1
            prev = prev.next
        
        curr, prev = l2, None
        square = -1
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
            square += 1
        
        res2 = 0
        while prev:
            res2 += prev.val * 10**square
            square -= 1
            prev = prev.next

        total = str(res1 + res2)
        dummy = ListNode()
        res = dummy
        for i in range(len(total) - 1, -1, -1):
            curr_val = int(total[i])
            dummy.next = ListNode(val = curr_val)
            dummy = dummy.next

        return res.next

