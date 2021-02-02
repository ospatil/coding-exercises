"""
LCM - Least Common Multiple - smallest number divisible by both given numbers
i/p: a=4, b=6 o/p: 12
i/p: a=12, b=15 o/p: 60
i/p: a=2, b=8 o/p: 8
i/p: a=3, b=7 o/p: 21

Time complexity:
lcmNaive: O(ab)
lcmEfficient: O(log(min(a,b)))
"""


"""
Start with maximum of two numbers and try to divide it by both numbers,
if not increament the number and try dividing again till one is found

"""


def lcmNaive(a, b):
    res = max(a, b)
    while True:
        if res % a == 0 and res % b == 0:
            return res
        res += 1
    return res


"""
Efficient implementation is based on the following formula:
a*b = gcd(a, b) * lcm(a, b)
Therefore amount of work done is for gcd + some constant work
"""


def lcmEfficient(a, b):
    return (a * b) / gcd(a, b)


def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)


def test_lcmNaive():
    assert lcmNaive(4, 6) == 12
    assert lcmNaive(12, 15) == 60
    assert lcmNaive(2, 8) == 8
    assert lcmNaive(3, 7) == 21


def test_lcmEfficient():
    assert lcmEfficient(4, 6) == 12
    assert lcmEfficient(12, 15) == 60
    assert lcmEfficient(2, 8) == 8
    assert lcmEfficient(3, 7) == 21
