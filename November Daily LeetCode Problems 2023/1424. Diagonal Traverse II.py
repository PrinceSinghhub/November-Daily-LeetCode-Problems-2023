class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:

        diags = defaultdict(list)
        for i in range(len(nums)):
            for j in range(len(nums[i])):
                diags[i + j].append(nums[i][j])
        result = []
        for i, j in diags.items():
            result += reversed(j)
        return result