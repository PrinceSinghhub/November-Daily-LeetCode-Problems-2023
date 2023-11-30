class Solution:

    def isValidVol(self, val):
        val = val.lower()
        data = "aeiou"
        if val in data:
            return True
        return False

    def sortVowels(self, s: str) -> str:

        myans = []
        conList = list(s)

        for chart in s:
            if self.isValidVol(chart):
                myans.append(chart)

        myans.sort()

        for i in range(len(conList)):

            if self.isValidVol(conList[i]):
                conList[i] = myans.pop(0)

        ans = ''.join(conList)
        return ans