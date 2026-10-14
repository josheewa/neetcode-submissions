class Solution:
    def largestRectangleArea(self, heights: list[int]) -> int:
        stk = deque()
        res = 0

        for r, height in enumerate(heights+[0]):
            while stk and heights[stk[-1]] > height:
                i = stk.pop()
                h = heights[i]
                l = stk[-1] if stk else -1
                w = r - l - 1
                res = max(res, w*h)
            stk.append(r)
        return res