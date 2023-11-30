class Solution:
    def maxCoins(self, piles):
        coins = 0
        piles.sort()
        data = len(piles) // 3

        for i in range(data):
            coins += piles[-2 - (2 * i)]

        return coins