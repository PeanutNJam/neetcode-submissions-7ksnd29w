class Solution:
    def get_minimizer(self, iterations: int, learning_rate: float, init: int) -> float:
        minimizer = init
        
        for _ in range(iterations):
            derivative = minimizer * 2
            minimizer -= derivative * learning_rate

        return round(minimizer, 5)