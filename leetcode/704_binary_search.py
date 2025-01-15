class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """

        Goal: Return the index of the target in nums array if exist, otherwise return -1.

        Binary search:
        - Sorted
        - Divide and conquer
        
        Runtime: O(logN)
        Spacetime: O(1)

        """


        left, right = 0, len(nums)-1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] > target:
                right = mid - 1
            elif nums[mid] < target:
                left = mid + 1
            else:
                return mid
        
        return -1