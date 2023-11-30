class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        return nums.sort() or max((nums[i] + nums[-(i + 1)]) for i in range(len(nums) // 2 + 1))
