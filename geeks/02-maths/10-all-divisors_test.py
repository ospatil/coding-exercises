"""
i/p: n = 15, o/p: 1, 3, 5, 15
i/p: n = 100, o/p: 1, 2, 4, 5, 10, 20, 25, 50, 100
i/p: n = 7, o/p: 1, 7
"""

"""
Naive solution
Time complexity: Theta(n)
Aux space: Theta(1)
"""


def allDivisorsNaive(n):
    res = []
    for i in range(1, n + 1):
        if n % i == 0:
            res.append(i)
    return res


"""
Efficient solution
Idea:
Divisors always appear in pairs.
Ex: 30 = (1, 30), (2, 15), (3, 10), (5, 6)
One of the divisors in every pair is <= sqrt(n)

Traverse through the numbers two times.
1. from 1 to sqrt(n), will give smaller divisors in a pair
2. from sqrt(n) to 1, n/i wil give the bigger divisor of a pair

Time complexity: Theta(n)
"""


def allDivisorsEfficient(n):
    res = []
    i = 1
    while i * i <= n:
        if n % i == 0:
            res.append(i)
        i += 1
    while i >= 1:
        if n % i == 0:
            # Needed for cases like 100, where there will be (10, 10) divisor pair
            if i != (n // i):
                res.append(n // i)
        i -= 1
    return res


def test_allDivisorsNaive():
    assert allDivisorsNaive(15) == [1, 3, 5, 15]
    assert allDivisorsNaive(100) == [1, 2, 4, 5, 10, 20, 25, 50, 100]
    assert allDivisorsNaive(7) == [1, 7]


def test_allDivisorsEfficient():
    assert allDivisorsEfficient(15) == [1, 3, 5, 15]
    assert allDivisorsEfficient(100) == [1, 2, 4, 5, 10, 20, 25, 50, 100]
    assert allDivisorsEfficient(7) == [1, 7]
