"""
Find the number appearing odd number of times in the given array.

i/p: arr = [4, 3, 4, 4, 4, 5, 5], o/p: 3
i/p: arr = [8, 7, 7, 8, 8], o/p: 8
"""


# Naive solution - O(n^2)
# iterate through the array and count the occurences of each element
def oneOddNaive(arr):
    for i in arr:
        count = 0
        for j in arr:
            if j == i:
                count += 1
        if count % 2 != 0:
            return i


"""
Efficient solution using XOR

Interesting properties of XOR
1. x ^ 0 = x
2. x ^ y = y ^ x (commutative)
3. x ^ (y ^ z) = (x ^ y) ^ z (associative)
4. x ^ x = 0

Idea:
XOR all numbers in array. The evenly occuring number will cancel
out each other. What is left is the odd occurring number.

Time complexity: O(n)
Aux space: O(1)
"""


def oneOddEfficient(arr):
    res = 0
    for i in arr:
        res ^= i
    return res


"""
Variation

Given an array of n numbers that has values in range [1..(n+1)]
and every number appearing exactly once, find the missing number.

i/p: arr = [1, 4, 3], o/p: 2
i/p: arr = [1, 5, 3, 2], o/p: 4

Solution:
If the array size is n, the range will be 1 to (n-1).
We do XOR of all numbers in range and then XOR with the numbers
in array. Since we are effectively XORing a number twice, once in
range and once in given array the will cancel out except the missing
number.
"""


def findMissing(arr):
    res = 0
    for i in range(1, len(arr) + 2):  # for range 1 to length+1 inclusive
        res ^= i  # xor the range
    for i in arr:
        res ^= i
    return res


def test_oneOddNaive():
    assert oneOddNaive([4, 3, 4, 4, 4, 5, 5]) == 3
    assert oneOddNaive([8, 7, 7, 8, 8]) == 8


def test_oneOddEfficient():
    assert oneOddEfficient([4, 3, 4, 4, 4, 5, 5]) == 3
    assert oneOddEfficient([8, 7, 7, 8, 8]) == 8


def test_findMissing():
    assert findMissing([1, 4, 3]) == 2
    assert findMissing([1, 5, 3, 2]) == 4
    assert findMissing([1, 2, 3, 4, 5]) == 6
