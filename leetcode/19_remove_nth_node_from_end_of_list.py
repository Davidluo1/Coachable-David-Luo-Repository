# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        """

        Goal: Remove the last nth node from the given linked list, and return its head.

        Approach:
        1. Get the length of the linked list.
        2. Iterate and remove nth end node.

        Runtime: O(2N)
        Spacetime: O(1)

        Approach 2:
        1. Two pointers, a fast pointer that is n blocks away from the slow pointer.
        2. Iterate till the fast pointer reach to the last node.
        3. Remove the node on the slow pointer.

        Runtime: O(N)
        Spacetime: O(1)
        
        """

        # if not head.next: return

        slow = fast = head

        for i in range(n): fast = fast.next

        if fast:
            while fast.next != None: slow, fast = slow.next, fast.next

        if fast == None: 
            head = head.next
            return head

        slow.next = slow.next.next

        return head


