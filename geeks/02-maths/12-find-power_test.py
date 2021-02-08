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
