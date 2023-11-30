class Solution:
    def minimumOneBitOperations(self, n: int) -> int:

        if not n:
            return 0
        if not (n & (n - 1)):
            return 2 * n - 1

        b = 1 << n.bit_length() - 1

        return self.minimumOneBitOperations((b >> 1) ^ b ^ n) + b