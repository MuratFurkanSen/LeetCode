class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        temp = head
        length = 0
        while temp is not None:
            length += 1
            temp = temp.next
        if length == 1:
            return None
        removeIndex = length - n
        temp = head
        for i in range(removeIndex-1):
            temp = temp.next
        if removeIndex == 0:
            head = temp.next
        elif temp.next.next is None:
            temp.next = None
        else:
            temp.next = temp.next.next
        return head
