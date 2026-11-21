class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return

        slow, fast = head, head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        second = slow.next
        slow.next = None

        prev, curr = None, second

        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        curr = head

        while prev:
            temp1 = curr.next
            temp2 = prev.next

            curr.next = prev
            prev.next = temp1

            curr = temp1
            prev = temp2


