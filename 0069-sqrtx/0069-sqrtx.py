class Solution:
    def mySqrt(self, x: int) -> int:
        
        if x < 0:
            return "Undefined"

        if x == 0:
            return 0

        # Initial guess
        guess = x / 2

        # Iterate until desired precision is achieved
        while True:
            new_guess = 0.5 * (guess + x / guess)
            if abs(guess - new_guess) < 1e-9:  # Adjust the desired precision as needed
                break
            guess = new_guess

        return int(new_guess)

