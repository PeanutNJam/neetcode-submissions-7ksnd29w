from collections import defaultdict
from typing import List

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj = defaultdict(list)

        # Sort in reverse so we can pop smallest later
        for src, dst in sorted(tickets, reverse=True):
            adj[src].append(dst)

        res = []

        def dfs(node):
            while adj[node]:
                nei = adj[node].pop()  # smallest lexical
                dfs(nei)
            res.append(node)

        dfs("JFK")
        return res[::-1]