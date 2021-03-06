# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
# a² + b² = c²
#
# For example, 3² + 4² = 9 + 16 = 25 = 5².
#
# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.

from math import sqrt

def solution():
    for a in range(1, 1000):
        for b in range(a, 1000):
            for c in range(b, 1000):
                if (a+b+c == 1000) and (a*a + b*b == c*c):
                    return a*b*c

if __name__ == '__main__':
    print(solution())
