# Given an integer n, return the largest number that contains exactly n digits.
def largestNumber(n):
    nstr = []
    for i in range(n):
        nstr.append('9')
    return int(''.join(nstr))
    
def largestNumber(n):
    return int(''.join('9'*n))
