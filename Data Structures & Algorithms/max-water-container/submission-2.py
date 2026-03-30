class Solution:
    def maxArea(self, heights: List[int]) -> int:
        res = 0
        l, r = 0, len(heights) - 1

        while r > l:
            max_area = min(heights[l], heights[r]) * (r - l)
            res = max(max_area, res)
            if heights[l] >= heights[r]:
                r -= 1
            else:
                l += 1

        return res
            