class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists: list[ListNode]) -> ListNode:
        if not any(lists):
            return None
        while lists.count(None) > 0:
            lists.remove(None)
        result = lists[0]
        for node in lists[1:]:
            temp = result
            prev = None
            while temp is not None and node is not None:
                if node.val >= temp.val:
                    prev = temp
                    temp = temp.next
                else:
                    if prev is None:
                        nextNode = node.next
                        result = node
                        prev = node
                        node.next = temp
                        node = nextNode
                    else:
                        nextNode = node.next
                        prev.next = node
                        node.next = temp
                        prev = prev.next
                        node = nextNode
            if temp is None:
                prev.next = node
        return result

s = Solution()
list1 = ListNode(1, ListNode(4, ListNode(5)))
list2 = ListNode(1, ListNode(3, ListNode(4)))
list3 = ListNode(2, ListNode(6))

print(s.mergeKLists([list1, list2, list3]))
