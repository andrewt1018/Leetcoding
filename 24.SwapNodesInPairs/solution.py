# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        
        array = []
        first = head
        second = head.next
        while first is not None and second is not None:
            array.append(second)
            array.append(first)
            first = second.next
            if first is not None:
                second = first.next
            else:
                second = None
                break
        if first is not None:
            array.append(first)
        head = array[0]
        current = head
        l = len(array)
        for i in range(1, l):
            current.next = array[i]
            current = current.next
        current.next = None
        return head
        