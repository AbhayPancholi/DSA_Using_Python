def BinarySearch(arr, x):
    l = 0  # lower bound
    u = len(arr) - 1  # upper bound
    mid = (l + u) // 2

    while l < u:
        if x == mid:
            return mid
        elif arr[mid] < x:
            l = mid + 1
        else:
            u = mid - 1
    return -1


# Driver Code
if __name__ == "__main__":
    arr = [2, 3, 4, 10, 40]
    x = 3

    # Function call
    result = BinarySearch(arr, x)
    if result != -1:
        print("Element is present at index", result)
    else:
        print("Element is not present in array")
