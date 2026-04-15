class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        alpha_map = {c: set() for w in words for c in w}
        indegree = {c: 0 for c in alpha_map}
        n = len(words)

        for i in range(n - 1):
            first, second = words[i], words[i + 1]
            minLen = min(len(first), len(second))
            if len(first) > len(second) and first[:minLen] == second[:minLen]:
                return ""
            for j in range(minLen):
                if first[j] != second[j]:
                    if second[j] not in alpha_map[first[j]]:
                        alpha_map[first[j]].add(second[j])
                        indegree[second[j]] += 1
                    break

        q = deque([c for c in indegree if indegree[c] == 0])
        res = []

        while q:
            char = q.popleft()
            res.append(char)
            for nei in alpha_map[char]:
                indegree[nei] -= 1
                if not indegree[nei]:
                    q.append(nei)
        if len(res) != len(indegree):
            return ""
            
        return "".join(res)




