class Solution:
    def climbStairs(self, n: int) -> int:
        cache = defaultdict(int)
        
        def topDown(val):
            if val in cache:
                return cache[val]
            if val == 0:
                return 1
            if val < 0:
                return 0
    
            res = topDown(val - 1) + topDown(val - 2)
            cache[val] = res
            return res

        return topDown(n)