class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, 1

        while numbers[r] + numbers[l] != target:
            if numbers[r] + numbers[l] == target:
                return [l + 1, r + 1]
            else:
                r += 1
                if r >= len(numbers):
                    l += 1
                    r = l + 1

        return [l + 1, r + 1]
