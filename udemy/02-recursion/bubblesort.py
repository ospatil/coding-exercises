def bubbleSort(arr):
    n = len(arr)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if arr[i] > arr[i + 1]:
                arr[i + 1], arr[i] = arr[i], arr[i + 1]


if __name__ == "__main__":
    arr = [4, 2, 7, 6, 8]
    bubbleSort(arr)
    print(f"bubbleSort(arr) = {arr}")
