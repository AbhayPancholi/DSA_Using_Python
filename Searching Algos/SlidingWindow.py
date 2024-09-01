# Example to demonstrate Sliding window where window size is 4.
def MaxSum(arr, k):
    if len(arr) < k:
        return -1

    max_sum = sum(arr[:k])
    window_sum = max_sum
    n = len(arr)
    for i in range(n - k):
        window_sum = window_sum - arr[i] + arr[i + k]
        max_sum = max(window_sum, max_sum)
    return max_sum


arr = [1, 4, 2, 10, 2, 3, 1, 0, 20]
k = 4
print(MaxSum(arr, k))
