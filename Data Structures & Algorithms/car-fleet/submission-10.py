class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        p_s = sorted(zip(position, speed), reverse=True)
        res = prev_time = 0
        

        for p, s in p_s:
            t = (target - p) / s

            if t > prev_time:
                res += 1
                prev_time = t
            

        return res


