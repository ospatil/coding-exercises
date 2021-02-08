"""
Given number n, print all primes numbers <= n
i/p: n = 10, o/p: 2, 3, 5, 7
i/p: n = 25, o/p: 2, 3, 5, 7, 11, 13, 17, 19, 23
"""

"""
Naive solution

Run loop for i  = 2 to n and check i is prime

Time complexity: O(n * sqrt(n))
"""


# def allPrimes(n):
#     res = []
#     for i in range(2, n + 1):  # n
#         if isPrime(i):  # isPrime is O(sqrt(n))
#             res.append(i)

"""
Sieve of Eratosthenes algorithm
1. Create a boolean array of size (n+1) will True values.
2. Make a pass through the array and
    1. Mark all slots that are multiples of 2 as False.
    2. Mark all slots that are multiples of 3 as False.
    3. Mark all slots that are multiples of 5 as False.
    ...
3. Pass through the array and the remaining "True" slots are prime.

Time complexity: O(n*log(log n))
Explanation:
Let’s assume our current prime number is 2. In the first iteration,
we’ll mark n/2 elements in the array. When our current prime number is 3, we
n/3 elementsmark . The total number times we runs the loop would be equal to:

n/2 + n/3 + n/5 + n/7 ...
= n * (1/2 + 1/3 + 1/5 + 1/7 ...)
It's a harmonic series, and for harmonic progression of the sum of primes
it's equal to log(log(n)).
= n * log(log(n))
"""


def sieveOfEratosthenes(n):
    isPrime = [True for i in range(n + 1)]
    for i in range(2, n + 1):
        if isPrime[i]:
            # Consider i = 2, it's prime
            # mark all multiples of 2 as False
            j = i * i  # set j = 4
            while j <= n:
                isPrime[j] = False
                j = j + i  # increment j = 6
    res = []
    for i in range(2, n + 1):
        if isPrime[i]:
            res.append(i)
    return res


def test_sieveOfEratosthenes():
    assert sieveOfEratosthenes(25) == [2, 3, 5, 7, 11, 13, 17, 19, 23]


# if __name__ == "__main__":
#     print(sieveOfEratosthenes(25))
