"""
i/p: n = 4, o/p: True
i/p: n = 6, o/p: False
"""


# Time complexity: Theta(log n)
def isPowerOfTwoNaive(n):
    if n == 0:
        return False
    while n != 1:
        if n % 2 != 0:
            return False
        n //= 2
    return True


"""
Efficient solution
Use Kirnighan's algorithm

Interesting point about powers of 2 is they have only 1 bit set.
So, count the set bits using Kirnighan's algorithm, if count is 1
it's power of 2 else not.

Time complexity: Theta(1)
"""


def isPowerOftwoKirnighan(n):
    # if n == 0, return False
    # n & (n - 1) will unset only set bit in power of two and result will be 0
    return n != 0 and (n & (n - 1)) == 0


def test_isPowerOfTwoNaive():
    assert isPowerOfTwoNaive(64) is True
    assert isPowerOfTwoNaive(126) is False


def test_isPowerofTwoKirnighan():
    assert isPowerOftwoKirnighan(64) is True
    assert isPowerOftwoKirnighan(126) is False
