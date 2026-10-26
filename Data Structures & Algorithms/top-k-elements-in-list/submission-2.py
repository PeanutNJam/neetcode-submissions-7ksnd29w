class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)
        for val in nums:
            count[val] += 1

        final = []
        for key, val in count.items():
            final.append((-val , key))

        heapq.heapify(final)
        res = []

        for _ in range(k):
            if final:
                res.append(heapq.heappop(final)[1])

        return res

