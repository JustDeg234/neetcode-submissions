# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow_ptr = fast_ptr = head #two pointers are init with node (singly, node is head)

        while fast_ptr and fast_ptr.next: #if the next node is null, short circuit conditional as list has no cycle (ends)
            slow_ptr = slow_ptr.next #Floyd's Cycle detection algorithm
            fast_ptr = fast_ptr.next.next
            if slow_ptr == fast_ptr:
                return True
        return False