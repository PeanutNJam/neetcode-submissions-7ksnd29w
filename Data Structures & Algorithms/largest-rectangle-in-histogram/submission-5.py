class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        maxAreas = []

        for i, h in enumerate(heights):
            start = i
            while stack and stack[-1][0] > h:
                nh, idx = stack.pop()
                maxAreas.append(nh * (i - idx))
                start = idx

            stack.append((h, start))
        
        maxArea = max(maxAreas) if maxAreas else 0
        for h, i in stack:
            maxArea = max(maxArea, h * (len(heights) - i))
        return maxArea