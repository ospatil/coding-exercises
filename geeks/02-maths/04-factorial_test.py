"""
Factorial n! = 1 * 2 * 3 * ... * (n-1) * n where n >=0

Problem:
i/p: 4, o/p: 24
i/p: 6, o/p: 720
i/p: 0, o/p: 1
i/p: 1, o/p: 1

Time Complexity:
factorialIter: Theta(n), Aux space: O(1)
factorialRec: Theta(n), Aux space: Theta(n)
"""


def factorialIter(n):
    # for n=0 or 1, res will be returned directly without loop execution
    res = 1
    for i in range(2, n + 1):  # n+1 because we need to include n too
        res = res * i
    return res


def factorialRec(n):
    if n <= 0:
        return 1
    return n * factorialRec(n - 1)


def test_factorialIter():
    assert factorialIter(4) == 24
    assert factorialIter(6) == 720
    assert factorialIter(0) == 1
    assert factorialIter(1) == 1


def test_factorialRec():
    assert factorialIter(4) == 24
    assert factorialIter(6) == 720
    assert factorialIter(0) == 1
    assert factorialIter(1) == 1
