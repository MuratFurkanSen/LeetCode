class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: ListNode, list2: ListNode) -> ListNode:
        if list1 is None and list2 is None:
            return None
        elif list1 is None:
            return list2
        elif list2 is None:
            return list1
        temp1 = list1
        temp2 = list2
        if temp1.val < temp2.val:
            result = ListNode(temp1.val)
            temp1 = temp1.next
        else:
            result = ListNode(temp2.val)
            temp2 = temp2.next
        temp3 = result

        while temp1 is not None and temp2 is not None:
            if temp1.val <= temp2.val:
                temp3.next = temp1
                temp1 = temp1.next
                temp3 = temp3.next
            else:
                temp3.next = temp2
                temp2 = temp2.next
                temp3 = temp3.next
        if temp1 is None:
            temp3.next = temp2
        else:
            temp3.next = temp1
        return result