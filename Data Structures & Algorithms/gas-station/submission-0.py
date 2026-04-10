class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        total_gas = gas + gas
        total_cost = cost + cost

        n = len(gas)
        for i in range(n):
            curr_gas = 0
            last = i + n
            for j in range(i, last):
                curr_gas += total_gas[j]
                if curr_gas < total_cost[j]:
                    break
                curr_gas -= total_cost[j]
                if j == last - 1:
                    return i

        return -1
            


