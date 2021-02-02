# a function that accepts a number and adds up all the numbers from 0 to number passed in
def recursiveRange(num):
    assert num >= 0 and int(num) == num, "Number must be positive integer"
    if num == 0:
        return 0
    else:
        return num + recursiveRange(num - 1)


if __name__ == "__main__":
    num = 3
    print(f"recursiveRange(num) = {recursiveRange(num)}")
    num = -3
    print(f"recursiveRange(num) = {recursiveRange(num)}")
