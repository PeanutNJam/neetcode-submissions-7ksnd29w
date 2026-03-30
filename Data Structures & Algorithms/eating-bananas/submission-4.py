class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        min_s, max_s = 1, max(piles)
        n = len(piles)

        while max_s >= min_s:
            res = 0
            mid_s = min_s + (max_s - min_s) // 2

            for p in piles:
                res += math.ceil(p/mid_s)

            if res <= h:
                max_s = mid_s - 1
            else:
                min_s = mid_s + 1

        return min_s
