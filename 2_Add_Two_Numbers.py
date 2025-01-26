# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        """

        Goal: Add the two numbers and return the sum as a linked list.

        Appraoch: Modify the l1 to the sum of l1 and l2.
        While there is a l1 and l2, find their node's sum.
        If one list reaches the end, keep the other linked list
        
        Runtime: O(N+M)
        Spacetime: O(1)


        """

        dumy = ListNode(None)
        head, total = dumy, 0

        while l1 or l2 or total // 10:
            # Check if there is node in l1 or l2
            value1 = l1.val if l1 else 0
            value2 = l2.val if l2 else 0

            total = value1 + value2 + total // 10

            dumy.next = ListNode(total % 10)
            dumy = dumy.next

            if l1: l1 = l1.next
            if l2: l2 = l2.next
        
        return head.next


