"""
i/p: n = 5, k = 1 o/p: True
5 = 101
      |_ kth bit(1)

i/p: n = 8, k = 2 o/p: False
8 = 1000
      |_ kth bit(2)
"""


def kthBitLeftShift(n, k):
    # 1 << (k - 1) will give us number with kth bit set
    if n & (1 << (k - 1)) != 0:
        return True
    return False


def kthBitRightShift(n, k):
    # move the kth bit to last position and then & with 1
    if (n >> (k - 1)) & 1 == 1:
        return True
    return False


def test_kthBitLeftShift():
    assert (kthBitLeftShift(13, 3)) is True
    assert (kthBitLeftShift(8, 2)) is False


def test_kthBitRightShift():
    assert (kthBitRightShift(13, 3)) is True
    assert (kthBitRightShift(8, 2)) is False
