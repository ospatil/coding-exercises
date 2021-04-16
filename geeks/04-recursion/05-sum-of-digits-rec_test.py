"""
Sum of digits using recursion (n >= 0)
i/p: n = 253, o/p: 10
i/p: n = 9987, o/p: 33
i/p: n = 10, o/p: 1

n % 10 will give the last digit of n
n // 10 will remove the last digit of n

Time complexity: Theta(no of digits)
Aux space: Theta(no of digits)
"""


def sumOfDigitsRec(n):
    if n == 0:
        return 0
    return n % 10 + sumOfDigitsRec(n // 10)


def test_sumOfDigitsRec():
    assert sumOfDigitsRec(253) == 10
    assert sumOfDigitsRec(9987) == 33
    assert sumOfDigitsRec(10) == 1


"""
Iterative solution of reference

Time complexity: Theta(no of digits)
Aux Space: Theta(1)
"""


def sumOfDigits(n):
    res = 0
    while n > 0:
        res += n % 10
        n //= 10
        print(f"res = {res}, n = {n}")
    return res


def test_sumOfDigits():
    assert sumOfDigits(253) == 10
    assert sumOfDigits(9987) == 33
    assert sumOfDigits(10) == 1
