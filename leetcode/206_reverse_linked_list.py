# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        
        Goal: Reverse the singly linked list, and return its new head.

        Approach 1:
        1. Iterate through and store all the elements in the linked list.
        2. Reverse the item list, and create a new linked list.
        Runtime: O(2N)
        Spacetime: O(N)

        Approach 2:
        1. Utilize the head pointer and a previous pointer to reverse each item in the linked list.
        Runtime: O(N)
        Spacetime: O(1)

        """

        if not head: return

        previous = None

        while head != None and head.next != None:
            next_node = head.next
            head.next = previous
            previous = head
            head = next_node
        
        head.next = previous
        return head