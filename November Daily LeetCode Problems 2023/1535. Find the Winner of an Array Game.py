class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:

        if k > len(arr):
            return max(arr)
        c = 0
        res = arr[0]
        while c < k:
            if arr[0] > arr[1]:
                big_elem = arr[0]
                small_elem = arr[1]
                idx = 1
            else:
                big_elem = arr[1]
                small_elem = arr[0]
                idx = 0
            arr.append(arr.pop(idx))
            if res == big_elem:
                c += 1
            else:
                c = 1
                res = big_elem
        return res