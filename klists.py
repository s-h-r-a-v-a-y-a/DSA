import heapq

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[Optional[ListNode]]
        :rtype: Optional[ListNode]
        """
        # Edge case: If the input list is empty, return None.
        if not lists or len(lists) == 0:
            return None

        # Initialize a min-heap to store the smallest nodes.
        heap = []

        # Push the head node of each non-empty linked list into the heap.
        # Use a tuple of (node value, list index, node reference) to avoid comparison errors.
        for i, node in enumerate(lists):
            if node:
                heapq.heappush(heap, (node.val, i, node))

        # Create a dummy node to simplify the process of building the merged linked list.
        dummy = ListNode()
        current = dummy  # Pointer to build the merged list.

        # Process the heap until it is empty.
        while heap:
            # Pop the smallest node from the heap.
            val, i, node = heapq.heappop(heap)

            # Add this node to the merged linked list.
            current.next = node
            current = current.next  # Move the pointer forward.

            # If the popped node has a next node, push it into the heap.
            if node.next:
                heapq.heappush(heap, (node.next.val, i, node.next))

        # Return the merged linked list, which starts at dummy.next.
        return dummy.next
