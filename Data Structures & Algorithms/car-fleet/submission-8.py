class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted(zip(position, speed), reverse=True)

        fleets = 0
        last_time = 0

        for p, s in cars:
            time = (target - p) / s   # exact time

            if time > last_time:      # forms new fleet
                fleets += 1
                last_time = time      # update slowest fleet time

        return fleets

