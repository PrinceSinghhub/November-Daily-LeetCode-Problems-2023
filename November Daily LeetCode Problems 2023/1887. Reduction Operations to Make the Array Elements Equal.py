class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        f = Counter(nums)
        s,ans=0,0
        for i in sorted(f.keys(), reverse=True)[:-1]:
            s += f[i]
            ans += s
        return ans