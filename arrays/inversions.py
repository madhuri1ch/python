"""
Given an array of integers arr[]. Find the Inversion Count in the array.
Two elements arr[i] and arr[j] form an inversion if arr[i] > arr[j] and i < j.

Inversion Count: For an array, inversion count indicates how far (or close) the array is from being sorted. If the array is already sorted then the inversion count is 0.
If an array is sorted in the reverse order then the inversion count is the maximum. 

Examples:

Input: arr[] = [2, 4, 1, 3, 5]
Output: 3
Explanation: The sequence 2, 4, 1, 3, 5 has three inversions (2, 1), (4, 1), (4, 3).
Input: arr[] = [2, 3, 4, 5, 6]
Output: 0
Explanation: As the sequence is already sorted so there is no inversion count.
Input: arr[] = [10, 10, 10]
Output: 0
Explanation: As all the elements of array are same, so there is no inversion count.

"""


def merge_and_count(arr, temp_arr, left, mid, right):
    # Initialize variables
    i = left    # Starting index for the left subarray
    j = mid + 1 # Starting index for the right subarray
    k = left    # Starting index to be used in the temporary array
    inv_count = 0

    # Traverse both subarrays
    while i <= mid and j <= right:
        if arr[i] <= arr[j]:
            temp_arr[k] = arr[i]
            i += 1
        else:
            # There are mid - i inversions, because all remaining elements in the
            # left subarray (arr[i], arr[i+1], ..., arr[mid]) are greater than arr[j].
            temp_arr[k] = arr[j]
            inv_count += (mid - i + 1)
            j += 1
        k += 1

    # Copy the remaining elements of the left subarray, if any
    while i <= mid:
        temp_arr[k] = arr[i]
        i += 1
        k += 1

    # Copy the remaining elements of the right subarray, if any
    while j <= right:
        temp_arr[k] = arr[j]
        j += 1
        k += 1

    # Copy the sorted subarray into the original array
    for i in range(left, right + 1):
        arr[i] = temp_arr[i]

    return inv_count


def merge_sort_and_count(arr, temp_arr, left, right):
    inv_count = 0
    if left < right:
        # Midpoint of the array
        mid = (left + right) // 2

        # Recursively sort and count for the left subarray
        inv_count += merge_sort_and_count(arr, temp_arr, left, mid)

        # Recursively sort and count for the right subarray
        inv_count += merge_sort_and_count(arr, temp_arr, mid + 1, right)

        # Merge the two subarrays and count inversions
        inv_count += merge_and_count(arr, temp_arr, left, mid, right)

    return inv_count


def count_inversions(arr):
    n = len(arr)
    temp_arr = [0] * n
    return merge_sort_and_count(arr, temp_arr, 0, n - 1)


# Example usage
arr = [1, 20, 6, 4, 5]
print(f"Number of inversions are: {count_inversions(arr)}")
