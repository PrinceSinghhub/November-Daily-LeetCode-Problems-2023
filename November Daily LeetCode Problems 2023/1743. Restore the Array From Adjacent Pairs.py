from collections import defaultdict

class Solution:
    def restoreArray(self, adjacentPairs):

        adj = defaultdict(list)
        for a, b in adjacentPairs:
            adj[a].append(b)
            adj[b].append(a)


        start = next(k for k, v in adj.items() if len(v) == 1)

        nums = []
        seen = set()

        def dfs(num):
            seen.add(num)
            nums.append(num)
            for next_num in adj[num]:
                if next_num not in seen:
                    dfs(next_num)

        dfs(start)
        return nums