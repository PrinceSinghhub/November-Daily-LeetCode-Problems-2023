class Solution:
    def numberOfWays(self, corridor: str) -> int:
        n = len(corridor)
        if n == 1:
            return 0
        d = defaultdict(int)
        numS = 0

        for i in range(n):
            if (numS == 0 or numS % 2 == 1) and corridor[i] == 'P':
                continue
            if corridor[i] == 'P':
                d[numS // 2] += 1
            else:
                numS += 1

        if numS == 0 or numS % 2:
            return 0
        if corridor[-1] == 'P':
            d[numS // 2] = 0

        ret = 1
        for v in d.values():
            ret *= (v + 1)
        return ret % (10 ** 9 + 7)