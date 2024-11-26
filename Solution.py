# This program adds two non-negative integers represented as linked lists in reverse order.
# The result is returned as a linked list in reverse order, with each node containing a single digit.


class Solution:
    def addTwoNumbers(self, l1, l2):
        # A dummy node to form the result linked list
        dummy = ListNode(0)
        current = dummy
        carry = 0

        while l1 or l2 or carry:
            # Extract values from the current nodes
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            # Calculate sum and carry
            total = val1 + val2 + carry
            carry = total // 10
            current.next = ListNode(total % 10)

            # Move the pointers
            current = current.next
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        # Return the head of the resulting list
        return dummy.next
