"""
Find two odd appearing numbers in array

i/p: [3, 4, 3, 4, 5, 4, 4, 6, 7, 7], o/p: [5, 6]
i/p: [20, 15, 20, 16], o/p: [15, 16]

Input array size is atleast 2 since there are 2 odd appearing numbers.
"""


# Naive solution: Theta(n^2)
# iterate on array, count how many times each element appears
def twoOddNaive(arr):
    res = []
    for i in arr:
        count = 0
        for j in arr:
            if i == j:
                count += 1
        if count % 2 != 0:
            res.append(i)
    return res


"""
Efficient solution using XOR: Theta(n)

1. Do XOR of all numbers in the given array.
All even appearing numbers will cancel each other.
The result will be XOR of two odd appearing numbers.

Taking first input, the XOR would be of 5 and 6.
5: 101
6: 110
XOR: 011
When there is a bit set in XOR, the correspoding bit will
be set in one number and unset in other.
We'll divide the input array into two:
a. numbers in which the bit is set: [3, 3, 5, 7, 7]
b. numbers in chich the bit is unset: [4, 4, 4, 4, 6]
Now our odd appearing numbers belog to one in each group.

2. Now we XOR both groups.
1st group XOR will give us first number and second the second.
"""


def twoOddEfficient(arr):
    xor, res1, res2 = 0, 0, 0
    for i in arr:
        xor ^= i
    sn = xor & ~(xor - 1)  # to get rightmost set bit
    for i in arr:
        if i & sn != 0:
            res1 ^= i
        else:
            res2 ^= i
    return [res1, res2]


def test_twoOddNaive():
    assert twoOddNaive([3, 4, 3, 4, 5, 4, 4, 6, 7, 7]) == [5, 6]
    assert twoOddNaive([20, 15, 20, 16]) == [15, 16]


def test_twoOddEfficient():
    assert twoOddEfficient([3, 4, 3, 4, 5, 4, 4, 6, 7, 7]) == [5, 6]
    assert twoOddEfficient([20, 15, 20, 16]) == [15, 16]
