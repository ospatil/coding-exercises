"""
08 - Check for prime
i/p: n = 23, o/p: True
i/p: n = 14, o/p: False
i/p: n = 101, o/p: True

First few prime numners: 2, 3, 5, 7, 11, 13, 17, 19 ...
1 is not considered a prime or composite and 2 is the only even prime.
"""

"""
isPrimeNaive
Time complexity:
The loop is running from 2 to n-1: O(n)
"""


def isPrimeNaive(n):
    if n == 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


"""
isPrimeEfficient
Idea: The divisors always appear in pairs.
30: (1, 30), (2, 15), (3,10), (5,6)
65: (1, 65), (5, 13)

If (x, y) is a pair:
x * y = n
and if x<= y
x * x <= n
Therefore, x <= sqrt(n)
So running the loop from 2 to sqrt(n)
Why upto sqrt(n): because if there is a divisor y > sqrt(n),
it's going to have a pair x that is <= sqrt(n)

Time complexity: O(sqrt(n))
"""


def isPrimeEfficient(n):
    if n == 1:
        return False
    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1
    return True


"""
isPrimeSuperEfficient

Idea:
Values of i for range n:
2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21...sqrt(n)
By checking n%2 == 0 and n % 3 == 0, we can bring down the number of
iterations to 1/3.
2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21...sqrt(n)
X,3,X,5,X,7,X,9,X ,11,X ,13,X ,15,X ,17,X ,19,X ,21...sqrt(n) by adding divisibility check by 2
X,X,X,5,X,7,X,X,X ,11,X ,13,X ,X ,X ,17,X ,19,X ,X ...sqrt(n) by adding divisibility check by 3

Time complexity:
It's still O(sqrt(n)) but it's 3 times faster than the efficient solution.
"""


def isPrimeSuperEfficient(n):
    if n == 1:
        return False
    if n == 2 or n == 3:
        return True
    if n % 2 == 0 or n % 3 == 0:  # divisibility check by 2 and 3
        return False
    i = 5  # after above checks we can directly start from 5
    while i * i <= n:
        # the first divisors are 5 and 5+2 i.e, 7, next 11 and 13 and so on
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6  # check the idea above 5+6 = 11, 11+6=17 and so on
    return True


def test_isPrimeNaive():
    assert isPrimeNaive(23) is True
    assert isPrimeNaive(14) is False
    assert isPrimeNaive(101) is True


def test_isPrimeEfficient():
    assert isPrimeEfficient(23) is True
    assert isPrimeEfficient(14) is False
    assert isPrimeEfficient(101) is True


def test_isPrimeSuperEfficient():
    assert isPrimeSuperEfficient(23) is True
    assert isPrimeSuperEfficient(14) is False
    assert isPrimeSuperEfficient(101) is True


"""
09 - Prime factors (divisors that are prime)
i/p: n = 12, o/p: 2,2,3 (2 divides 12 twice)
i/p: n = 13, o/p: 13
i/p: n = 315, o/p: 3,3,5,7

If you multiply all prime factors, you get the original number back.
"""


"""
primeFactorsNaive

Time complexity:
Outer loop: O(n)
The prime check: O(n)
inner loop: log n

O(n^2 log n)
"""


def primefactorsNaive(n):
    pf = []
    for i in range(2, n):
        if isPrimeSuperEfficient(i):
            # why another variable, because multiple powers of i can divide n
            # say for 12, 2 divides 12 and 4 also divides 12
            # we assign 2 to x, we add it to list of prime factors and
            # change x to next power i.e 4, check if it's divisible by 4,
            # if yes, add 2 once more to the list and continue with next power
            x = i
            while n % x == 0:  # is n divisible by 2 for our example
                pf.append(i)
                x = x * i  # we try out next power
    return pf


"""
primeFactorsEfficient

Idea:
1. The divisors always appear in pairs.
   So if we can iterate from 2 to sqrt(n), we'll get prime factor.
2. A number can be written as multiplication of powers of prime factors.
   12 = 2^2 * 3
   450 = 2^1 * 3^2 * 5^2
So, the algorithm is loop from 2 to sqrt(n) and find the first prime factor
Once found, divide n repeatedly while n is still divisible.
Then move to the next prime factor and repeat.
"""


def primeFactorsEfficient(n):
    pf = []
    if n <= 1:
        return pf
    i = 2
    while i * i <= n:
        while n % i == 0:
            pf.append(i)
            n //= i
        i += 1
    # case for last prime factor with power 1, ex: for n=84 n will be 7
    # when the above loop terminates, so we add 7 to prime factors
    if n > 1:
        pf.append(n)
    return pf


"""
primeFactorsSuperEfficient
Applying the same optimization as isPrimeSuperEfficient

Time complexity: Theta(sqrt(n))
"""


def primeFactorsSuperEfficient(n):
    pf = []
    if n <= 1:
        return pf
    while n % 2 == 0:
        pf.append(2)
        n //= 2
    while n % 3 == 0:
        pf.append(3)
        n //= 3
    i = 5
    while i * i <= n:
        while n % i == 0:
            pf.append(i)
            n //= i
        while n % (i + 2) == 0:
            pf.append(i + 2)
            n = n // (i + 2)
        i += 6
    if n > 3:
        pf.append(n)
    return pf


def test_primeFactorsNaive():
    assert primefactorsNaive(12) == [2, 2, 3]
    assert primefactorsNaive(84) == [2, 2, 3, 7]
    assert primefactorsNaive(450) == [2, 3, 3, 5, 5]


def test_primeFactorsEfficient():
    assert primeFactorsEfficient(12) == [2, 2, 3]
    assert primeFactorsEfficient(84) == [2, 2, 3, 7]
    assert primeFactorsEfficient(450) == [2, 3, 3, 5, 5]


def test_primeFactorsSuperEfficient():
    assert primeFactorsSuperEfficient(12) == [2, 2, 3]
    assert primeFactorsSuperEfficient(84) == [2, 2, 3, 7]
    assert primeFactorsSuperEfficient(450) == [2, 3, 3, 5, 5]


# if __name__ == "__main__":
#     print(primeFactorsEfficient(450))
