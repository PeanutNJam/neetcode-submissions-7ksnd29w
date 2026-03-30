class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted(zip(position, speed), reverse=True)
        res = 0
        last_time = 0

        for p, s in cars:
            t = (target - p) / s

            if t > last_time:
                res += 1
                last_time = t

        return res
