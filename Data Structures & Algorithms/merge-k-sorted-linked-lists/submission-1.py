# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        while len(lists) > 1:
            mergedList = []
            for i in range(0, len(lists), 2):
                n1 = lists[i]
                if i + 1 >= len(lists):
                    n2 = None
                else:
                    n2 = lists[i + 1]

                mergedList.append(self.combine(n1, n2))
            lists = mergedList

        return lists[0] if lists else None




    def combine(self, n1, n2):
        dummy = ListNode(0)
        curr = dummy
        
        while n1 and n2:
            if n1.val >= n2.val:
                curr.next = n2
                curr = curr.next
                n2 = n2.next
            else:
                curr.next = n1
                curr = curr.next
                n1 = n1.next

        if n1:
            curr.next = n1
        elif n2:
            curr.next = n2

        return dummy.next

