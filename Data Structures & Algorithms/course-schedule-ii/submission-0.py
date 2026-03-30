class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        indegree = [0] * numCourses
        adjTree = [[] for _ in range(numCourses)]
        res = []

        for dst, src in prerequisites:
            indegree[dst] += 1
            adjTree[src].append(dst)

        q = deque()
        now = 0

        for i in range(numCourses):
            if not indegree[i]:
                q.append(i)

        while q:
            curr = q.popleft()
            now += 1
            res.append(curr)

            for nei in adjTree[curr]:
                indegree[nei] -= 1
                if not indegree[nei]:
                    q.append(nei)

        return res if now == numCourses else []
