# nth fibonacci number: 0, 1, 1, 2, 3, 5, 8
def fib(num):
    if num < 2:
        return num
    else:
        return fib(num - 1) + fib(num - 2)


if __name__ == "__main__":
    num = 4
    print(f"fib(num) = {fib(num)}")
