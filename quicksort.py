"""Quick sort algorithm"""

def partition(input_array, low, high):
    """Partition the array using pivot."""
    i = (low - 1)
    pivot = input_array[high]

    for j in range(low, high):
        if input_array[j] <= pivot:
            i += 1
            input_array[i], input_array[j] = input_array[j], array[i]
    input_array[i + 1], input_array[high] = input_array[high], input_array[i + 1]
    return (i + 1)

