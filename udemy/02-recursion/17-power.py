# equation: x^n = x * x^(n-1)
def power(x, n):
    assert n >= 0 and int(n) == n, "power must be non-negative integer"
    if n == 0:
        return 1
    else:
        return x * power(x, n - 1)


if __name__ == "__main__":
    x, n = 2, 5
    print(f"{x}^{n} = {power(x, n)}")
    x, n = 3, 4
    print(f"{x}^{n} = {power(x, n)}")
