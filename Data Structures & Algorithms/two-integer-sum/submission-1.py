class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        idx_map = defaultdict(int)
        for i, num in enumerate(nums):
            rem = target - num
            if rem in idx_map:
                return[idx_map[rem], i]
            idx_map[num] = i


        

                