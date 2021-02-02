"""
Problem:
i/p: n = 78987, o/p: True
i/p: n = 8668, o/p: True
i/p: n = 8, o/p: True; a single digit number is always palindrome
i/p: n = 21, o/p: False

n >= 0

Hint:
We find reverse of given number and compare.
Remove the last digit using mod and assemble the reverse number
by multiplying by 10 and adding the last digit

Time Complexity:
Theta(d) where d is number of digits
"""


def palindromeNumber(n):
    tmp = n
    rev = 0
    while tmp != 0:
        ld = tmp % 10  # last digit
        rev = rev * 10 + ld
        tmp //= 10
    return rev == n


def test_palindromeNumber():
    assert palindromeNumber(78987) is True
    assert palindromeNumber(8668) is True
    assert palindromeNumber(8) is True
    assert palindromeNumber(21) is False
