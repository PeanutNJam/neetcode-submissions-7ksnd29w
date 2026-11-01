class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea = 0
        stack = []

        for i, h in enumerate(heights):
            start = i
            while stack and stack[-1][1] > h:
                ni, nh = stack.pop()
                maxArea = max(maxArea, (i - ni) * nh)
                start = ni

            stack.append((start, h))

        n = len(heights)
        for idx, h in stack:
            maxArea = max(maxArea, (n - idx) * h)

        return maxArea
