class Solution:
    def byMathCheckPoint(self, time, dir):

        abs_A = abs(dir[0] - dir[2])
        abs_B = abs(dir[1] - dir[3])
        MaxPoint = max(abs_A, abs_B)

        if MaxPoint > time or (MaxPoint == 0 and (time < 2 and time > 0)):
            return False
        else:
            return True

    def isReachableAtTime(self, sx: int, sy: int, fx: int, fy: int, t: int) -> bool:

        dir = [sx, sy, fx, fy]
        return self.byMathCheckPoint(t, dir)

