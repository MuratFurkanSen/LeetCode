class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        subList = list()
        if head is None:
            return head
        temp = head
        while True:
            for __ in range(k):
                if temp is None:
                    return head
                subList.append(temp)
                temp = temp.next
            i = 0
            while i < len(subList):
                subList[i].next = subList[i - 1].next if i == 0 else subList[i - 1]
                i += 1

            if len(subList) == k:

                if subList[0] == head:
                    head = subList[-1]
                else:
                    prev.next = subList[-1]

                i += 1
            if len(subList) == k:
                prev = subList[0]
                temp = subList[0].next
                subList.clear()
            else:
                return head
