print("fun1(3)", end=" = ")


def fun1(n):
    if n == 0:
        return
    print(n, end=" ")
    fun1(n - 1)
    print(n, end=" ")


"""
o/p: 3 2 1 1 2 3
Trace:
fun1(3)
|- 3
|- fun1(2)
|    |- 2
|    |- fun1(1)
|    |    |- 1
|    |    |- fun1(0)
|    |    |    |- return
|    |    |- 1
|    |- 2
|- 3
"""
print(fun1(3))

print("fun2(3)", end=" = ")


def fun2(n):
    if n == 0:
        return
    fun2(n - 1)
    print(n, end=" ")
    fun2(n - 1)


"""
o/p: 1 2 1 3 1 2 1
Trace:
fun2(3)
| fun2(2)
|   |- fun2(1)
|   |   |-fun2(0)
|   |   |   |-return
|   |   |- 1
|   |   |- fun2(0)
|   |   |   |- return
|   |- 2
|   |- fun2(1)
|   |   |- fun2(0)
|   |   |   |- return
|   |   |- 1
|   |   |- fun2(0)
|   |   |   |- return
|- 3
|- fun2(2)
"""
print(fun2(3))


def fun3(n):
    if n == 1:
        return 0
    else:
        return 1 + fun3(n // 2)


"""
o/p: 4
trace:
fun3(16)
|- 1 + fun3(8)
|       |- 1 + fun3(4)
|       |       |- 1 + fun3(2)
|       |       |       |- 1 + fun3(0)
|       |       |       |       | return 0
|       |       |       | - return 1
|       |       | return 1 + 1 = 2
|       | - return 1 + 2 = 3
| return 1 + 3 = 4

Consider the execution:
fun3(1) = 0
fun3(2) = 1 + fun3(1) = 1
fun3(4) = 1 + fun3(2) = 2
fun3(8) = 1 + fun3(4) = 3
fun3(16) = 1 + fun3(8) = 4

This is a log function. It returns log(floor(n)) to the base 2.
"""
print(f"fun3(16) = {fun3(16)}")

print("fun4(7)", end=" = ")


def fun4(n):
    if n == 0:
        return
    fun4(n // 2)
    print(n % 2, end=" ")


"""
o/p= 1 1 1
trace:
fun4(7)
|- fun4(3)
|   |- fun4(1)
|   |   |- fun4(0)
|   |   |   |- return
|   |   |- 1
|   |- 1
|- 1

This function prints binary representatation of n.
"""
print(fun4(7))
