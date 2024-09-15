class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: [ListNode], l2: [ListNode]) -> [ListNode]:
        carry = 0
        sum = (l1.val + l2.val + carry) % 10
        carry = (l1.val + l2.val + carry) // 10
        head = ListNode(sum)
        l1 = l1.next
        l2 = l2.next
        temp = head
        while l1 is not None and l2 is not None:
            sum = (l1.val + l2.val + carry) % 10
            carry = (l1.val + l2.val + carry) // 10
            temp.next = ListNode(sum)
            temp = temp.next
            l1 = l1.next
            l2 = l2.next
        while l1 is not None:
            sum = (l1.val + carry) % 10
            carry = (l1.val + carry) // 10
            temp.next = ListNode(sum)
            temp = temp.next
            l1 = l1.next
        while l2 is not None:
            sum = (l2.val + carry) % 10
            carry = (l2.val + carry) // 10
            temp.next = ListNode(sum)
            temp = temp.next
            l2 = l2.next
        if carry > 0:
            temp.next = ListNode(carry)
        return head
