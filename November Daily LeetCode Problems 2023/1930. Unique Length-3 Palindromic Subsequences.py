class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        l=[]
        p=len(s)
        count=0
        for i in range(len(s)):
            if s[i] not in l:
                j=s[::-1].index(s[i])
                j=p-j-1
                count=count+len(set(s[i+1:j]))
                l.append(s[i])
            else:
                continue
        return count