class Solution:
    def countNicePairs(self, nums: List[int]) -> int:
        res = 0
        mod = (10 ** 9 + 7)
        groups = collections.defaultdict(int)
        for num in nums:
            current = int(str(num)[::-1]) - num
            res += groups[current]
            groups[current] += 1

        return res % mod