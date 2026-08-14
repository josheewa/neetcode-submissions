class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        forward = [1 for _ in range(n)]
        backward = [1 for _ in range(n)]

        for i in range(1, n):
            forward[i] = forward[i-1] * nums[i-1]
            backward[n-i-1] = backward[n-i] * nums[n-i]
        
        return [forward[i] * backward[i] for i in range(n)]
