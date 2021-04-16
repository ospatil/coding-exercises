"""
Print n to 1 using recursion (n >= 1)
i/p: n = 5, o/p: 5, 4, 3, 2, 1

Time complexity: Theta(n)
Aux space: Theta(n)
"""

print("printNto1(n)")


def printNto1(n):
    if n == 0:
        return
    else:
        print(n)
        printNto1(n - 1)


print(printNto1(5))


"""
Print 1 to n using recursion
i/p: n = 4, o/p: 1 2 3 4
Time compexity: Theta(n)
Aux space: Theta(n)
"""

print("print1ToN(n)")


def print1ToN(n):
    if n == 0:
        return
    print1ToN(n - 1)
    print(n)


print1ToN(5)

"""
Tail recursion
Consider the printNto1 function compared to print1toN.
It would be more efficienton modern computers because it's tail-recursive.
In tail-recursive functions, recursion is the last thing parent function does.
It is efficient because the caller doesn't have to save the state.
When the modern compilers detect tail-recursion, make optimization that looks
something like this:

def printNto1(n):
    if n == 0:  # Add a label start at this point
        return
    print(n)
    printNto1(n - 1) # replace this with n -= 1 goto start

This optimization is called tail-call elimination.
"""

"""
Converting a non tail-recursive function into one
Below is print1toN converted to tail-recursion.

Not all non tail-recursive functions can be converted to
tail-recursive version.
Ex - In mergesort the merge has to happen after sort while quicksort is
tail-recursive.
"""


def print1ToNTailrec(n, k):
    if n == 0:
        return
    print(k)
    print1ToNTailrec(n - 1, k + 1)


"""
Question: is the following factorial function tail-recursive?
No, it's not.
"""


def fact(n):
    if n == 0 or n == 1:
        return 1
    return n * fact(n - 1)


"""
Converting above function to tail-recursive.
"""


def factTailRec(n, k):
    if n == 0 or n == 1:
        return 1
    return factTailRec(n - 1, k * n)
