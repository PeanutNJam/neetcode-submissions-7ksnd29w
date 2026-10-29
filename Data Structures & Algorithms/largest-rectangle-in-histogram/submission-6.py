class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        maxArea = 0

        for i, h in enumerate(heights):
            start = i
            while stack and stack[-1][0] > h:
                nh, ni = stack.pop()
                maxArea = max(nh * (i - ni), maxArea)
                start = ni

            stack.append((h, start))

        for h, i in stack:
            maxArea = max(maxArea, h * (len(heights) - i))

        return maxArea