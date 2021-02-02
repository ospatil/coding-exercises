# equation
# f(n) = n mod 2 + 10 * f(n/2)
def decimalToBinary(n):
    assert int(n) == n, "n should be integer"
    if n == 0:
        return 0
    else:
        return n % 2 + 10 * decimalToBinary(int(n / 2))


if __name__ == "__main__":
    print(f"decimalToBinary(10) = {decimalToBinary(10)}")
