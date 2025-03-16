import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        if len(nums) == 1: return nums[0]

        window = nums[:k]
        heapq.heapify(window)

        for num in nums[k:]:
            if num > window[0]:
                heapq.heappop(window)
                heapq.heappush(window,num)

        return window[0]
