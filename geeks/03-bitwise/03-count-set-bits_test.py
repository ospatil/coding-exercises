"""
i/p: n = 5, o/p: 2
i/p: n = 3, o/p: 2
i/p: n = 13, o/p: 3
"""


# Time complexity: Theta(total bits in n)
def countSetBitsNaive(n):
    res = 0
    while n > 0:
        print(f"n = {n}")
        # any odd number & 1 is 1 and any even number & 1 is 0
        res += n & 1  # equal to if n%2 == 0: res += 1
        print(f"res = {res}")
        n >>= 1  # equal to n//2
    return res


"""
Brian Kirnighan's algorithm

Idea:
Bitwise ANDing a number x with a (x - 1) resets to 0 in the result all
the bits that are right of 1st set bit in x.

Tracing:
Tracing the implementation for n = 40

1st iteration:
n = 40          101000
n = 39          100111
n & (n - 1)     100000 (32)

2nd iteration
n = 32          100000
n = 31          011111
n & (n - 1)     000000 (0)

Time complexity:
Theta(set bit count)
"""


def countSetBitsKernighan(n):
    res = 0
    while n > 0:
        n &= n - 1
        res += 1
    return res


"""
Lookup table method

Idea:
Divide input n into 8-bit chunks.
Pre-calculate a lookup table with numbers from 0 to 255 (because
8-bit numbers can have value between 0 to 2^7 - 1 i.e. 255) where
table[i] = no of set bits in i
Ex: table[0] = 0, table[1] = 1, table[2] = 1 and so on.

Time complexity: Theta(1)
"""


def countSetBitsTable(n):
    res = 0
    table = []
    table.append(0)
    for i in range(1, 256):
        table.append((i & 1) + table[i // 2])

    # n & 0xff (255 = 0b11111111) will give us last 8 digits
    # get the number of set bits for the number represented
    # by those last 8 digits
    res = res + table[n & 0xFF]
    n >>= 8  # move to next 8 bits
    res = res + table[n & 0xFF]
    n >>= 8  # move to next 8 bits
    res = res + table[n & 0xFF]
    n >>= 8  # move to next 8 bits
    res = res + table[n & 0xFF]

    return res


def test_countSetBitsNaive():
    assert countSetBitsNaive(5) == 2
    assert countSetBitsNaive(3) == 2
    assert countSetBitsNaive(13) == 3


def test_countSetBitsKernighan():
    assert countSetBitsKernighan(5) == 2
    assert countSetBitsKernighan(3) == 2
    assert countSetBitsKernighan(13) == 3


def test_countSetBitsTable():
    assert countSetBitsTable(5) == 2
    assert countSetBitsTable(3) == 2
    assert countSetBitsTable(15) == 4
