# Calculate the number pi with a given accuracy d.
# Example:
# when d = 0.001, π = 3.141    10^{-1} ≤ d ≤10^{-10}

import math

piNum = math.pi
# Next row allows us get the count of digits in fractional part of accuracy
accuracy = len(input('Please enter the required accuracy d (10^{-1} ≤ d ≤10^{-10}): ')) - 2
print(f'Pi number, using round function: {round(piNum, accuracy)}')

# If there is a problem to use built in functions, we can use slices, something like:
print(f'Pi number, using slices: {str(piNum)[:accuracy + 2]}')
