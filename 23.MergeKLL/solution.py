# https://leetcode.com/problems/merge-k-sorted-lists/

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class MinHeap:
    def __init__(self):
        self.array = []
        self.length = 0
    
    def insert(self, node):
        if node is None:
            return
        if self.length == 0:
            self.array.append(node)
            self.length += 1
            return
        else:
            self.array.append(node)
            self.length += 1
            self.swimup(self.length - 1)
    
    def pop(self):
        if self.length == 0:
            return None
        else:
            ret = self.array[0]
            self.array[0] = self.array[0].next
            if self.array[0] == None:
                self.array[0] = self.array[self.length - 1]
                self.array[self.length - 1] = None
                self.length -= 1
                self.swimdown(0)
            else:
                self.swimdown(0)
            return ret
    
    def get_length(self):
        return self.length

    def swimup(self, index):
        if index == 0:
            return
        node = self.array[index]
        parent_ind = (index - 1) // 2
        parent = self.array[parent_ind]
        if parent.val > node.val:
            self.swap(index, parent_ind)
            self.swimup(parent_ind)
    
    def swimdown(self, index):
        node = self.array[index]
        l_child_ind = 2 * index + 1
        r_child_ind = 2 * index + 2
        # If no children
        if l_child_ind >= self.length and r_child_ind >= self.length:
            return
        # If right child exists
        elif l_child_ind >= self.length:
            r_child = self.array[r_child_ind]
            if r_child.val < node.val:
                self.swap(index, r_child_ind)
                self.swimdown(r_child_ind)
        # If left child exists
        elif r_child_ind >= self.length:
            l_child = self.array[l_child_ind]
            if l_child.val < node.val:
                self.swap(index, l_child_ind)
                self.swimdown(l_child_ind)
        # If both children exist
        else:
            l_child = self.array[l_child_ind]
            r_child = self.array[r_child_ind]
            if node.val <= l_child.val and node.val <= r_child.val:
                return
            if l_child.val > r_child.val:
                self.swap(index, r_child_ind)
                self.swimdown(r_child_ind)
            elif l_child.val < r_child.val:
                self.swap(index, l_child_ind)
                self.swimdown(l_child_ind)
            else:
                self.swap(index, l_child_ind)
                self.swimdown(l_child_ind)

    def swap(self, i, j):
        temp = self.array[i]
        self.array[i] = self.array[j]
        self.array[j] = temp
    
    def print_heap(self):
        print(self.array)


class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        k = len(lists)
        if k == 0:
            return None

        heap = MinHeap()
        # Create the heap
        for node in lists:
            heap.insert(node)
        head = heap.pop()
        current = head
        while heap.get_length() != 0:
            current.next = heap.pop()
            current = current.next
        return head