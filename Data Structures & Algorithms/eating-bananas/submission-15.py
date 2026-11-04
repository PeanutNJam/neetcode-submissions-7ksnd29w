class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        total = sum(piles)
        max_speed = max(piles)
        speed_needed = math.ceil(total/h)

        while speed_needed <= max_speed:
            curr = 0
            mid = speed_needed + (max_speed - speed_needed) // 2
            for b in piles:
                curr += math.ceil(b/mid)
            
            if curr <= h:
                max_speed = mid - 1
            else:
                speed_needed = mid + 1

        return speed_needed







        

