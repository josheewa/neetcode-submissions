class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stk = deque()

        res = 0

        for r, h in enumerate(heights + [0]):
            while stk and heights[stk[-1]] > h:
                idx = stk.pop()
                bar = heights[idx]

                l = stk[-1] if stk else -1
                w = r - l - 1
                res = max(res, w*bar)
            stk.append(r)
        return res