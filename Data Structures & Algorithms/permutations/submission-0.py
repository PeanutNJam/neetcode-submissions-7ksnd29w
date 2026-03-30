class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        self.res = []
        self.backtrack([], nums, [False] * len(nums))
        return self.res

    def backtrack(self, perm: List[int], nums: List[int], curr: List[bool]):
        if len(perm) == len(nums):
            self.res.append(perm.copy())
            return

        for i in range(len(nums)):
            if not curr[i]:
                perm.append(nums[i])
                curr[i] = True
                self.backtrack(perm, nums, curr)
                perm.pop()
                curr[i] = False

    
