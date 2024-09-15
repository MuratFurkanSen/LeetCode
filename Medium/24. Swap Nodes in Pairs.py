class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if head is None or head.next is None:
            return head
        temp = head.next
        head.next = temp.next
        temp.next = head
        head = temp
        temp = head.next
        while temp.next is not None and temp.next.next is not None:
            temp1 = temp.next
            temp2 = temp.next.next
            temp.next = temp2
            temp1.next = temp2.next
            temp2.next = temp1
            temp = temp.next.next
        return head
