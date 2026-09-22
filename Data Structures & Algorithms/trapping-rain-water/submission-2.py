class Solution:
    def trap(self, height: List[int]) -> int:
        w = len(height)
        if w < 3: return 0

        leftmax = [height[0]] * w
        rightmax = [height[w-1]] * w

        for i in range(1, w):
            leftmax[i] = max(leftmax[i-1], height[i])
        for i in range(w-2, -1, -1):
            rightmax[i] = max(rightmax[i+1], height[i])
            
        res = 0
        for i in range(w):
            res += min(leftmax[i], rightmax[i]) - height[i]
        return res