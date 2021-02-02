def isOdd(num):
    if num % 2 == 0:
        return False
    else:
        return True


def someRecursive(arr, cb):
    if len(arr) == 0:
        return False
    if not cb(arr[0]):
        return someRecursive(arr[1:], cb)
    return True


if __name__ == "__main__":
    arr = [1, 2, 3, 4]
    print(f"someRecursive({arr}, isOdd) = {someRecursive(arr, isOdd)}")
    arr = [4, 2, 6, 4]
    print(f"someRecursive({arr}, isOdd) = {someRecursive(arr, isOdd)}")
    arr = []
    print(f"someRecursive({arr}, isOdd) = {someRecursive(arr, isOdd)}")
