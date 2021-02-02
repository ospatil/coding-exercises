def fibonacci(n):
    assert n >= 0 and int(n) == n, "n can only be positive integer"
    if n in [0, 1]:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


if __name__ == "__main__":
    print(f"fibonacci(7) = {fibonacci(7)}")
