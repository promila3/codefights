# Promila Agarwal
#N is divisible by divisor.
#N is less than or equal to bound.
#N is greater than 0.
def maxMultiple(divisor, bound):
    N = bound
    while N != 0 :
        if N % divisor == 0 :
            return N
        N -=1
    return N
