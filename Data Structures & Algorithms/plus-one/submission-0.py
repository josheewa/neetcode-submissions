class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num = 0
        
        for i in range(len(digits)):
            num += digits[len(digits)-i-1]* 10**i
        num += 1

        s = str(num)
        res = []
        for c in s:
            res.append(int(c))
        return res
