"""Quick sort algorithm"""

def partition(input_array, low, high):
    """Partition the array using pivot."""
    i = (low - 1)
    pivot = input_array[high]

    for j in range(low, high):
        if input_array[j] <= pivot:
            i += 1
            input_array[i], input_array[j] = input_array[j], input_array[i]
    input_array[i + 1], input_array[high] = input_array[high], input_array[i + 1]
    return (i + 1)

def quick_sort(input_array, low, high):
    """Iterative Quick sort."""
    if low < high:
        index = partition(input_array, low, high)
        quick_sort(input_array, low, index - 1)
        quick_sort(input_array, index + 1, high)
