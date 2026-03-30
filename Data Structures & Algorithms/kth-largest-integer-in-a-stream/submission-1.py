class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.maxHeap = [-num for num in nums]
        heapq.heapify(self.maxHeap)
        self.k = k
        

    def add(self, val: int) -> int:
        heapq.heappush(self.maxHeap, -val)
        curr = self.maxHeap.copy()

        if len(self.maxHeap) < self.k:
            while curr:
                res = -heapq.heappop(curr)
        else:
            count = 0
            while count != self.k:
                count += 1
                res = -heapq.heappop(curr)

        return res
        
