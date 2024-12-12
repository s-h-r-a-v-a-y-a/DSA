class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        # Dummy node to simplify handling of head swaps
        dummy = ListNode(0)
        dummy.next = head
        current = dummy

        # Traverse the list in pairs
        while current.next and current.next.next:
            # Identify the two nodes to swap
            first = current.next
            second = current.next.next
            
            # Swap the nodes
            first.next = second.next
            second.next = first
            current.next = second
            
            # Move the pointer two nodes ahead
            current = first

        # Return the new head of the list
        return dummy.next
