# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        list1 = []
        list2 = []

        while l1:
            list1.append(l1.val)
            l1 = l1.next

        while l2:
            list2.append(l2.val)
            l2 = l2.next

        total = 0
        n1, n2 = len(list1) - 1, len(list2) - 1

        for i in range(len(list1) - 1, -1, -1):
            total += list1[i] * (10 ** n1)
            n1 -= 1

        for i in range(len(list2) - 1, -1, -1):
            total += list2[i] * (10 ** n2)
            n2 -= 1

        if not total:
            return ListNode(val=0)

        dummyNode = ListNode()
        curr = dummyNode
        while total:
            curr.next = ListNode(val=total % 10)
            total //= 10
            curr = curr.next

        return dummyNode.next
            





        

        
            