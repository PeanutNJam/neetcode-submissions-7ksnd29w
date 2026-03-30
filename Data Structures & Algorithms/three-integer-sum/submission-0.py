class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        count_map = defaultdict(int)

        res = []

        for num in nums:
            count_map[num] += 1

        n = len(nums)

        for i in range(n):
            count_map[nums[i]] -= 1

            if i and nums[i] == nums[i - 1]:
                continue

            for j in range(i + 1, n):
                count_map[nums[j]] -= 1
                if j - 1 > i and nums[j] == nums[j - 1]:
                    continue
                
                target = 0 - nums[i] - nums[j]
                
                if count_map[target] > 0:
                    res.append([nums[i], nums[j], target])

            for j in range(i + 1, n):
                count_map[nums[j]] += 1

        return res