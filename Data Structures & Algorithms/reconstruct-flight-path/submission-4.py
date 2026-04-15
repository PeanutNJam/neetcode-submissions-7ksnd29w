class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        tickets.sort(reverse=True)
        adj_map = defaultdict(list)
        start = "JFK"
        res = []

        for src, dst in tickets:
            adj_map[src].append(dst)

        def dfs(src):
            while adj_map[src]:
                dst = adj_map[src].pop()
                dfs(dst)
            res.append(src)

        dfs(start)
        return res[::-1]
