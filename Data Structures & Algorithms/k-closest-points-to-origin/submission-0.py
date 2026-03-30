class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        min_heap = []
        res = []

        for x, y in points:
            heapq.heappush(min_heap, [(x**2 + y**2)**0.5, [x, y]])

        for _ in range(k):
            res.append(heapq.heappop(min_heap)[1])

        return res
