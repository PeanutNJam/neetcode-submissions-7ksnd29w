class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)

        while r >= l:
            mid = l + (r - l) // 2
            curr = 0
            for p in piles:
                curr += math.ceil(p/mid)
            if curr > h:
                l = mid + 1
            else:
                r = mid - 1

        return l

