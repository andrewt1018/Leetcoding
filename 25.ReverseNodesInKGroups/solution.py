# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head is None:
            return None
        array = []
        current = head
        length = 0
        while current is not None:
            subarray = []
            full = True
            for _ in range(k):
                if current is None:
                    full = False
                    break
                subarray.append(current)
                current = current.next
            if full:
                subarray = subarray[::-1]
                for elem in subarray:
                    array.append(elem)
                    length += 1
            else:
                for elem in subarray:
                    array.append(elem)
                    length += 1
                break
        new_head = array[0]
        current = new_head
        for i in range(1, length):
            current.next = array[i]
            current = current.next
        current.next = None
        return new_head

