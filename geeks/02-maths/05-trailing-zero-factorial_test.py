"""
i/p: 5, o/p: 1 (becase 5! = 120, trailing zeros = 1)
i/p: 10, o/p: 2 (becase 10! = 362800, trailing zeros = 2)

Time complexity:
trailingZerosFactNaive: Theta(n)
trailingZerosEfficient: Theta(log n)
"""


def trailingZerosFactNaive(n):
    fact = 1
    for i in range(2, n + 1):
        fact = fact * i
    res = 0
    while fact % 10 == 0:
        res += 1
        fact //= 10
    return res


"""
The idea is count how many pairs of 2's and 5's we have in prime factorization
since 2 and 5 together for a trailing zero.
Another fact is number of 5's will be less than number of 2's, therefore
counting only 5's will be sufficient.
Consider the factorial: 1 * 2 * 3 *4 * 5 * 6 * 7 * 8 * 9 * 10 ... n
Every 5th number will have at least one 5 as prime factor, so for any number n,
there are at least floor(n/5) 5's in the prime factorization.
Some numbers will have more than one 5 as a prime factor, Ex: 25 has 2, 125
has 3.
So the formula will be: floor(n/5) + floor(n/25) + floor(n/125)
When we do floor(n/5), it counts one 5 occurence.
floor(n/25) counts the other factor and so on.
"""


def trailingZerosEfficient(n):
    res = 0
    i = 5
    while i <= n:
        res = res + n // i
        i *= 5
    return res


def test_trailingZerosFactNaive():
    assert trailingZerosFactNaive(5) == 1
    assert trailingZerosFactNaive(10) == 2


def test_trailingZerosFactEffective():
    assert trailingZerosFactNaive(5) == 1
    assert trailingZerosFactNaive(10) == 2
    assert trailingZerosFactNaive(251) == 62
