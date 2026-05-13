class Solution:
    def maxArea(self, heights: List[int]) -> int:
    
        l = 0
        r = len(heights) - 1
        max_area = 0
        while l < r:
            min_height = min(heights[l], heights[r])
            distance = r - l
            area = min_height * distance 
            max_area = max(max_area, area)
            if min_height == heights[l]:
                l += 1

            if min_height == heights[r]:
                r -= 1
        return max_area

