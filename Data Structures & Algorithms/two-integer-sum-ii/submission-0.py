class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        p = 0
        q = len(numbers) - 1

        while numbers[p] + numbers[q] != target:
            if numbers[p] + numbers[q] > target:
                q -= 1
            else:
                p += 1
        return [p+1, q+1]