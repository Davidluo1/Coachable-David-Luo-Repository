# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        """

        Goal: Check whether the subRoot is a subtree of a binary tree.

        Approach:
        1. Iterate through each node of the binary tree and compare with the subRoot.

        Runtime: O(N)
        Spacetime: O(1)

        """

        # return str(subRoot) in str(root)

        # Function checking whether the current root equals to the subRoot
        def helper(root, subRoot):
            if not root and not subRoot: return True
            elif root and subRoot:
                return root.val == subRoot.val and helper(root.left, subRoot.left) and helper(root.right, subRoot.right)
            else: return False  # one node is empty
            
        return bool(root and subRoot) and (helper(root, subRoot) or self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot))



