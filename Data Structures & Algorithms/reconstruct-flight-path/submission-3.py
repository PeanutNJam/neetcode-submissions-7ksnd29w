class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj_list = defaultdict(list)
        res = []
        start = "JFK"

        for src, dst in sorted(tickets, reverse=True):
            adj_list[src].append(dst)

        def dfs(node):

            while adj_list[node]:
                nei = adj_list[node].pop()
                dfs(nei)

            res.append(node)

        dfs(start)
        return res[::-1]
            
        
            