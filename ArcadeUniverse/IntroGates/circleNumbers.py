# Promila Agarwal
# Find the directly opposite number in a circle of n numbers from firstNumber
def circleOfNumbers(n, firstNumber):
    mid = n/2
    return ((firstNumber + mid) % n)
