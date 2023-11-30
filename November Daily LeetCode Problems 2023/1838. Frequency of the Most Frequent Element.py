from collections import Counter
class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()
        i = 0
        cursum = 0
        res = 0
        for j, num in enumerate(nums):
            cursum += num
            while cursum + k < (j-i+1)*num:
                cursum -= nums[i]
                i += 1
            res = max(res, j-i+1)
        return res