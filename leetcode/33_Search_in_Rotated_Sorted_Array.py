class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """

        Goal: Return the index of the target in nums array if exist, return -1 otherwise.

        Log N = binary search = divide and conquer

        Approach:
        1. Check if the nums array is rotated by comparing the value at index 0 and -1.
        2. Compare the value of left index to the current value of mid index.
        3. Return the index if target value is found, or update the current mid index.
        4. If left intersects the right index, return -1.

        """

        # Divide and conquer
        left, right = 0, len(nums)-1

        while left <= right:
            mid = (left + right) // 2

            # Base check
            if nums[mid] == target:
                return mid
            
            # No rotation
            if nums[left] <= nums[mid]:
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            # Rotation
            else:
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
        
        return - 1


