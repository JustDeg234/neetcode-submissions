

class Solution:
    def mergeTwoLists(self, l1: ListNode | None, l2: ListNode | None) -> ListNode | None:
        #Building the output singly linked list
        head = ListNode() #dummy node, stays at head
        tail = head #moving tail

        while l1 and l2:
            if l1.val < l2.val:
                tail.next = l1
                l1 = l1.next #move forward in list (why we check edge case of l1=None)
            else:
                tail.next = l2
                l2 = l2.next
            tail = tail.next

        #Until here, last element wouldn't be used as either l1 or l2 ran out before the other
        if l1:
            tail.next = l1
        elif l2:
            tail.next = l2

        return head.next #dummy val is null