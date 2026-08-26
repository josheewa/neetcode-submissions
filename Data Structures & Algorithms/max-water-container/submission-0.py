class Solution:
    def maxArea(self, heights: List[int]) -> int:
        p = 0
        q = len(heights) - 1

        res = 0

        while p < q:
            water = (q-p) * min(heights[p], heights[q])
            res = max(water, res)
            if heights[p] < heights[q]:
                p += 1
            else:
                q -= 1

        return res