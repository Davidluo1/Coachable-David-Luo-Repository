class Solution:
    def trap(self, height: List[int]) -> int:
        """

        Goal: Compute the maximum water the elevation map could trap.

        Easy case:
        if the length of the height array is less than 3, it cannot trap any water.

        Approach:
        Keep iterating through the array if the right wall is smaller than the left wall.
        Keep track of the walls in between.
        Each iteration can contain up to left wall height of water.
        Ignore walls that is 0.
        Stop when the left wall index reaches to the length of the array minus 2.

        Runtime: O(N^2)
        Spacetime: O(1)
        Approach 2:
        Runtime: O(N)
        Spacetime: O(1)

        """
        

        max_volume, left, right = 0, 0, len(height)-1
        l_wall, r_wall = height[left], height[right]


        while left < right:
            if height[left] < height[right]:
                left += 1
                l_wall = max(l_wall, height[left])
                max_volume += (l_wall - height[left])               
            else:
                right -= 1
                r_wall = max(r_wall, height[right])
                max_volume += (r_wall - height[right])
        
        return max_volume


