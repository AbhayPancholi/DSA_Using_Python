# Demonstration of two pointers
def TwoPointers(arr, x):
    l = 0
    u = len(arr) - 1
    while l < u:
        if arr[l] + arr[u] == x:
            return True
        elif arr[l] + arr[u] < x:
            l += 1
        else:
            u -= 1


if __name__ == "__main__":
    # array declaration
    arr = [2, 3, 5, 8, 9, 10, 11]

    # value to search
    val = 8

    # size of the array
    # arrSize = len(arr)

    # array should be sorted before using the two-pointer technique
    # arr.sort()

    # Function call
    print(TwoPointers(arr, val))
