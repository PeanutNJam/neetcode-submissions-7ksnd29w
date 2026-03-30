class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        res = 0

        while r > l:
            max_area = min(heights[l], heights[r]) * (r - l)
            res = max(res, max_area)
            if heights[r] >= heights[l]:
                l += 1
            else:
                r -= 1
        
        return res