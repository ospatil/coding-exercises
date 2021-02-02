from math import floor, log10

"""
Time complexity:
If d is the number of digits in n, the loop will run d times.
Therefore Theta(d)
"""


def countDigitsIter(n):
    count = 0
    while n > 0:
        n = n // 10
        count += 1
    return count


def countDigitsRec(n):
    if n == 0:
        return 0
    return 1 + countDigitsRec(n // 10)


def countDigitsLog(n):
    return floor(log10(n) + 1)


def test_countDigitsIter():
    assert countDigitsIter(4123) == 4


def test_countDigitsRec():
    assert countDigitsRec(123) == 3


def test_countDigitsLog():
    assert countDigitsLog(1234) == 4
