"""
i/p: x = 2, n = 3, o/p: 8
i/p: x = 3, n = 4, o/p: 81
i/p: x = 5, n = 0, o/p: 1
i/p: x = 5, n = 1, o/p: 5
"""


# Time complexity = heta(n)
def powerNaive(x, n):
    res = 1
    for i in range(n):
        res *= x
    return res


"""
Efficient recursive solution
Idea:
power(x, n) =
    if n % 2 = 0
        power(x, n/2) * power(x, n/2)
    else
        power(x, n - 1) * x

Tracing one execution:
powerRec(3, 5)
|_tmp = powerRec(3, 2) = 3 * 3
|       |_tmp = powerRec(3, 1) = 3
|       |       |_tmp = powerRec(3, 0) = return 1
|       |       |_ return 3
|       |_ return 3 * 3
|_return (3 * 3) * (3 * 3) * 3

Time complexity:
The recurrence equation = T(n) = T(floor(n/2)) + Theta(1)
We are dividing n by two in each step, so the height of tree is
log n. There is constant work at each step = Theta(log n)
Aux space: Theta(log n)
"""


def powerRec(x, n):
    if n == 0:
        return 1
    tmp = powerRec(x, n // 2)
    tmp = tmp * tmp
    if n % 2 == 0:
        return tmp
    else:
        return tmp * x


"""
Efficient iterative solution - binary exponentiation

Idea:
1. We split the work using the binary representation of the exponent n.
    ex: 3^13 = 3^1101 = 3^8 * 3^4 * 3^1
2. We iterate through the bits of n, and every set bit, consider it as
    multiplier of corresponding power of x.
    Ex: x = 3, n = 10
    n = 10 = 1          0       1       0
             3^4        3^3     3^2     3^1
        i.e  3*3*3*3    3*3*3   3*3     3
3. We can iterate through bits of a number from LSB to MSB in O(log n) time.
    while n > 0:
        if n % 2 != 0
            # bit is 1
        else
            # bit is 0
        n //= 2

Time complexity: O(log n)
Aux space: O(1)

"""


def powerIter(x, n):
    res = 1
    while n > 0:
        if n & 1:  # same as n % 2 != 0 but more efficient
            res = res * x
        x *= x  # moving to next higher bit, so it's value is x * x
        n = n >> 1  # same as n //= 2 but more efficient
    return res


def test_powerNaive():
    assert powerNaive(2, 3) == 8
    assert powerNaive(3, 4) == 81
    assert powerNaive(5, 0) == 1
    assert powerNaive(5, 1) == 5


def test_powerRec():
    assert powerRec(2, 3) == 8
    assert powerRec(3, 4) == 81
    assert powerRec(5, 0) == 1
    assert powerRec(5, 1) == 5


def test_powerIter():
    assert powerIter(2, 3) == 8
    assert powerIter(3, 4) == 81
    assert powerIter(5, 0) == 1
    assert powerIter(5, 1) == 5
