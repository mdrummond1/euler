'''
Problem 3

The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143?
'''

def factor(term):
    factors = [i for i in range(1, term) if term % i == 0]
    print(factors)
    return factors

num = 12
factors = factor(num)
factors.reverse()
print(factors)
top = factors[0]
print("max is %i" % (top))