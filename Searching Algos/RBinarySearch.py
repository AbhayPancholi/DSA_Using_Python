def RecursiveBinarySearch(arr, l, u, x):

    while l <= u:
        mid = (l + u) // 2

        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            return RecursiveBinarySearch(arr, mid + 1, u, x)
        else:
            return RecursiveBinarySearch(arr, l, mid - 1, x)
    return -1


if __name__ == "__main__":
    arr = [2, 3, 4, 10, 40]
    x = 23

    # Function call
    result = RecursiveBinarySearch(arr, 0, len(arr) - 1, x)

    if result != -1:
        print("Element is present at index", result)
    else:
        print("Element is not present in array")
