"""
GCD or HCF - given a and b, find largest number that divides both
i/p: a=4, b=6 o/p: 2
i/p: a=100, b=200 o/p: 100
i/p: a=17, b=13 o/p: 1

Variation: Given a rectangle a * b, find sides of the largest square
tile that can fill the rectangle.

Time complexity:
gcdNaive: O(min(a, b))
gcdEuclidean: O(log b) Aux space: O(log b)
gcdEuclideanIter: O(log b) Aux space: O(1)
"""


"""
Start with minimum of two numbers and try divinding by that number,
if not try dividing by smaller number till one is found

"""


def gcdNaive(a, b):
    res = min(a, b)
    while res > 0:
        if a % res == 0 and b % res == 0:
            break
        res -= 1
    return res


def gcdEuclidean(a, b):
    # if b > a, the first recursive call is going to flip the arguments
    # gcdEuclidean(12, 15) -> b = 15 and a%b = 12 so the first
    # recursive call will be gcdEuclidean(15, 12)
    if b == 0:
        return a
    return gcdEuclidean(b, a % b)


def gcdEuclideanIter(a, b):
    tmp = 0
    while b != 0:
        tmp = a % b
        a, b = b, tmp
    return a


def test_gcdNaive():
    assert gcdNaive(4, 6) == 2
    assert gcdNaive(100, 200) == 100
    assert gcdNaive(17, 13) == 1


def test_gcdEuclidean():
    assert gcdEuclidean(4, 6) == 2
    assert gcdEuclidean(100, 200) == 100
    assert gcdEuclidean(17, 13) == 1


def test_gcdEuclideanIter():
    assert gcdEuclideanIter(4, 6) == 2
    assert gcdEuclideanIter(100, 200) == 100
    assert gcdEuclideanIter(17, 13) == 1
