class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        maxArea = 0
        stack = []

        for i in range(n + 1):
            print("i: ", i)
            while stack and (i == n  or heights[stack[-1]] >= heights[i]):
                height = heights[stack.pop()]
                print("height: ", height)
                width = i if not stack else i - stack[-1] - 1
                print("width: ", width)
                maxArea = max(maxArea, height * width)
                print("max area: ", maxArea)
            stack.append(i)
        return maxArea