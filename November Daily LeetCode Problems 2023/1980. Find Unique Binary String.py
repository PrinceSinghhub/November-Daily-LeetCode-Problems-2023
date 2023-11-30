from itertools import product


class Solution:

    def geenrateAllPair(self, n, ans, nums):

        if n == 0:
            nums.append(ans)
            return nums
        else:
            self.geenrateAllPair(n - 1, ans + "0", nums)
            self.geenrateAllPair(n - 1, ans + "1", nums)

    def findDifferentBinaryString(self, nums):

        # using module

        #         minPair = ['0', '1']
        n = len(nums)

        #         combinations = list(product(minPair, repeat=n))

        #         possStr = [''.join(combination) for combination in combinations]

        # return possStr

        # using recursino
        pairs = []
        self.geenrateAllPair(n, "", pairs)
        for i in pairs:
            if i not in nums:
                return i