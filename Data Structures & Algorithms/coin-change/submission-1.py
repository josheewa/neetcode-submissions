class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        a = {c:1 for c in coins}
        small = min(coins)

        def aux(n):
            if n == 0: return 0
            if n < small: return -1
            if n in a: return a[n]

            vals = []
            for c in coins:
                temp = aux(n-c)
                if temp < 0: a[n-c] = -1
                else: vals.append(temp)
            if not vals: return - 1
            res = min(vals) + 1

            a[n] = res
            return res
        return aux(amount)