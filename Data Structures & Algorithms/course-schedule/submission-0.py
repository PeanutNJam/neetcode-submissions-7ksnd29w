class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indegree = [0] * numCourses
        adjTree = [[] for _ in range(numCourses)]


        for src, dst in prerequisites:
            indegree[dst] += 1
            adjTree[src].append(dst)

        q = deque()

        for i in range(numCourses):
            if not indegree[i]:
                q.append(i)

        res = 0
        while q:
            curr = q.popleft()
            res += 1

            for nei in adjTree[curr]:
                indegree[nei] -= 1
                if not indegree[nei]:
                    q.append(nei)


        return res == numCourses

