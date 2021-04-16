"""
Sum of natural numbers using recursion
i/p: 3, o/p: 6
i/p: 4, o/p: 10
i/p: 5, o/p: 15

Time complexity: Theta(n)
Aux space: Theta(n)
"""


def sumRec(n):
    if n == 0:
        return 0
    return n + sumRec(n - 1)


def test_sumRec():
    assert sumRec(3) == 6
    assert sumRec(4) == 10
    assert sumRec(5) == 15
