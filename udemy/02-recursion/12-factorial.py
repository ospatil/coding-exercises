def factorial(n):
    assert n >= 0 and int(n) == n, "The number can only be positive integer."
    if n in [0, 1]:
        return 1
    else:
        return n * factorial(n - 1)


if __name__ == "__main__":
    print(f"factorial(4) = {factorial(4)}")
    # print(f"factorial(-2) = {factorial(-2)}")
    # print(f"factorial(1.5) = {factorial(1.5)}")
