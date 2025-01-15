class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        """

        Goal: Return the minimun speed of k to eat all the bananas within h hours.

        total of bananas
        h hours -> h times

        speed * h >= total of bananas

        total // h = speed
        
        Easy case:
        If h equals to the banana piles size, return the max banana pile.

        Approach:
        1. Sort the banana piles.
        2. If h is bigger than the banana piles size, calculate its difference and find the dth largest element.
        3. Check if the total (speed * h) is equal or bigger than the total bananas in the piles.
        4. If not, add one to the speed until (speed * h) is equal or bigger.
        5. Return the final speed.  


        """
        

        left, right = 1, max(piles)

        # def dumy(cur_speed):
        #     return sum(ceil(pile/cur_speed) for pile in piles) <= h

        while left < right:
            cur_speed = (left + right) // 2
            temp = sum(ceil(pile/cur_speed) for pile in piles)
            # temp = 0
            # for pile in piles:
            #     temp += ceil(pile/cur_speed)
            if temp <= h:
                right = cur_speed
            else:
                left = cur_speed + 1

        return left

        # if h == len(piles): return piles[0]
        # else:
        #     d_largest = h % len(piles)
 
        #     if h < 2*len(piles):
        #         speed = piles[d_largest]
        #     else:
        #         if d_largest == 0:
        #             speed = piles[-1]
        #         else:
        #             speed = piles[-d_largest]
        #     total = sum(piles)

        #     while speed * h < total:
        #         speed += 1

        # return speed



