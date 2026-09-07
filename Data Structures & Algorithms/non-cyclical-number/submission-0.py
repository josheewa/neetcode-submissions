class Solution:
    def isHappy(self, n: int) -> bool:
        prev = n
        seen = set()
        while True:
            ds = str(n)
            n = 0
            for d in ds:
                n += int(d)**2
            prev = n
            if n in seen:
                if n == 1:
                    return True
                else:
                    return False
            
            seen.add(n)