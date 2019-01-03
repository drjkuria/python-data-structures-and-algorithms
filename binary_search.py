"""Binary search algorithm using iteration."""

def binary_search_iterative(input_array, value):
    """Iterative binary search."""
    low = 0
    high = len(input_array) - 1
    while low <= high:
        mid = (low + high) // 2
        if input_array[mid] == value:
            return mid
        elif input_array[mid] < value:
            low = mid + 1
        else:
            high = mid - 1
    return -1