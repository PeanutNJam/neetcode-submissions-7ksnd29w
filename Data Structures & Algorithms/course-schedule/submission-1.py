class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indegree = [0] * numCourses
        adj_tree = defaultdict(list)

        for src, dst in prerequisites:
            adj_tree[dst].append(src)
            indegree[src] += 1

        q = deque([])
        for c in range(numCourses):
            if not indegree[c]:
                q.append(c)
        res = 0
        while q:
            res += 1
            curr = q.popleft()
            for nei in adj_tree[curr]:
                indegree[nei] -= 1
                if not indegree[nei]:
                    q.append(nei)

        return res == numCourses
        


            

