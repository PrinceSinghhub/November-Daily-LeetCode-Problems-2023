class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        ps = [0 for i in range(len(nums))]

        ps[0] = nums[0]
        for i in range(1, len(nums)):
            ps[i] = ps[i - 1] + nums[i]

        ans = []
        for i in range(len(nums)):

            lft = 0
            if i != 0:
                lft = (i) * nums[i] - ps[i - 1]

            rgt = ps[-1] - ps[i] - ((len(nums) - i - 1) * nums[i])

            ans.append(lft + rgt)

        return ans