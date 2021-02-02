def productOfArray(arr):
    if len(arr) == 0:
        return 1
    else:
        return arr[0] * productOfArray(arr[1:])


if __name__ == "__main__":
    arr = [1, 2, 3]
    print(f"productOfArray(arr) = {productOfArray(arr)}")
    arr = [2]
    print(f"productOfArray(arr) = {productOfArray(arr)}")
    arr = []
    print(f"productOfArray(arr) = {productOfArray(arr)}")
