class Solution:
    def knightDialer(self, n: int) -> int:
        # paths represents every key we can go to from given key
        # -1 is starting condition, we can start from any key
        paths = {-1: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 0: [4, 6], 1: [6, 8], 2: [7, 9],
                 3: [4, 8], 4: [0, 3, 9], 5: [], 6: [0, 1, 7], 7: [2, 6], 8: [1, 3], 9: [2, 4]}

        return self.helper(paths, n, -1, {}) % (10 ** 9 + 7)

    def helper(self, paths, idx, curr, cache):
        if (idx, curr) in cache:
            return cache[(idx, curr)]
        if idx == 0:
            return 1

        count = 0
        for num in paths[curr]:
            count += self.helper(paths, idx - 1, num, cache)

        cache[(idx, curr)] = count
        return count