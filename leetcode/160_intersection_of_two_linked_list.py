# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        """

        Goal: Return the node at which the two linked-list intersect, return null otherwise.

        Appraoch 1:
        1. Iterate both linked list, keep track of all visited items.
        2. End the loop if a intersect item is found.

        Runtime: O((N+M)K)
        Spacetime: O(N+M)

        Approach 2:
        1. Iterate through one linked list and store all disctinct elements.
        2. Iterate through the other list and check for instersections.
        
        Runtime: O(N+MK)
        Spacetime: O(N)

        Pattern: If the last node of listA and listB are the same, there is an intersection.

        """

        memo = set()

        while headA:
            memo.add(headA)
            headA = headA.next

        while headB:
            if headB in memo: return headB
            headB = headB.next
        
        return None


        memo = []
        
        while headA or headB:
            if headA == headB or headA in memo: return headA
            elif headB in memo: return headB
            else:
                if headA:
                    memo.append(headA)
                    headA = headA.next
                if headB:
                    memo.append(headB)
                    headB = headB.next
            
        return None