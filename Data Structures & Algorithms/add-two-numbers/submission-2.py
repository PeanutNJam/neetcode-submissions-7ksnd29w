# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        prev1, curr1 = None, l1
        prev2, curr2 = None, l2
        res1 = []
        res2 = []

        while curr1:
            res1.append(curr1.val)
            curr1 = curr1.next

        while curr2:
            res2.append(curr2.val)
            curr2 = curr2.next

        val1 = val2 = 0
        n1, n2 = 10**(len(res1) - 1), 10**(len(res2) - 1)

        for i in range(len(res1) -1, -1, -1):
            val1 += n1 * res1[i]
            n1 //= 10

        for i in range(len(res2) -1, -1, -1):
            val2 += n2 * res2[i]
            n2 //= 10

        total = val1 + val2
        dummy = ListNode()
        curr = dummy
        while total:
            val = total % 10
            curr.next = ListNode(val=val)
            total //= 10
            curr = curr.next

        return dummy.next if dummy.next else ListNode()

        

        
            