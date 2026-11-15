class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = deque([])
        res = []
        l = r = 0

        while r < len(nums):
            while q and nums[q[-1]] < nums[r]:
                q.pop()
            q.append(r)

            while l > q[0]:
                q.popleft()

            if r - l + 1 >= k:
                l += 1
                res.append(nums[q[0]])         
            
            r += 1

        return res



