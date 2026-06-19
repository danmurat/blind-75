class Solution:
    def maxArea(self, heights: List[int]) -> int:
        p1: int = 0
        p2: int = len(heights) - 1
        max_area: int = 0

        while p1 < p2:
            min_height: int = min(heights[p1], heights[p2])
            width: int = p2 - p1
            area: int = width * min_height
            if max_area < area:
                max_area = area
            
            # if distance is always going to shorten, we move the p with the smallest height
            # for a chance at a bigger height (which might have a bigger area!)
            if heights[p1] <= heights[p2]: p1 += 1
            else: p2 -= 1

        return max_area