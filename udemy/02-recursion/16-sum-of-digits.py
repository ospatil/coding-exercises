# equation f(n) = n%10 + f(n/10)
def sumOfDigits(n):
    assert n >= 0 and int(n) == n, "n must be positive integer"
    if n == 0:
        return 0
    else:
        return n % 10 + sumOfDigits(int(n / 10))


if __name__ == "__main__":
    print(f"sumOfDigits(123) = {sumOfDigits(123)}")
