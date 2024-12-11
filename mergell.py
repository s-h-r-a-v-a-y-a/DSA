# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        # Create a dummy node to simplify edge cases
        dummy = ListNode()
        current = dummy

        # Traverse both lists and merge them
        while list1 and list2:
            if list1.val <= list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next

        # Directly attach whichever list is remaining (either list1 or list2)
        current.next = list1 if list1 else list2

        # Return the merged list starting from the node after dummy
        return dummy.next

# Helper function to create a linked list from a Python list
def create_linked_list(lst):
    dummy = ListNode()
    current = dummy
    for val in lst:
        current.next = ListNode(val)
        current = current.next
    return dummy.next

# Helper function to print a linked list
def print_linked_list(head):
    current = head
    while current:
        print(current.val, end=" -> ")
        current = current.next
    print("None")

# Example input
list1 = create_linked_list([1, 2, 4])
list2 = create_linked_list([1, 3, 4])

# Merge the two lists
solution = Solution()
merged_head = solution.mergeTwoLists(list1, list2)

# Output the merged list
print_linked_list(merged_head)
