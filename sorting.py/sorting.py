# Main Program
X = [1, 5, 6, 4, 3, 3, 7, 7, 7, 9, 0, 1, 1, 3, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0]


# Merge Sort
def merge_sort_modified(array):
    if len(array) <= 1:
        return array
    mid = len(array) // 2
    left_half = merge_sort_modified(array[:mid])
    right_half = merge_sort_modified(array[mid:])
    
    merged_array = []
    i = j = 0
    
    # Merge the arrays
    while i < len(left_half) and j < len(right_half):
        if left_half[i] <= right_half[j]:
            merged_array.append(left_half[i])
            i += 1
        else:
            merged_array.append(right_half[j])
            j += 1

    # Append any remaining elements
    merged_array.extend(left_half[i:])
    merged_array.extend(right_half[j:])
    return merged_array


# Merge Sort Execution
merge_sorted_modified = merge_sort_modified(X)
print("Sorted using Modified Merge Sort:", merge_sorted_modified)


# Quick Sort
def quick_sort_modified(array):
    if not array:
        return []
    pivot_index = len(array) // 2
    pivot_value = array[pivot_index]
    smaller = [item for index, item in enumerate(array) if item < pivot_value]
    equal = [item for index, item in enumerate(array) if item == pivot_value]
    larger = [item for index, item in enumerate(array) if item > pivot_value]
    
    return quick_sort_modified(smaller) + equal + quick_sort_modified(larger)


# Quick Sort Execution
quick_sorted_modified = quick_sort_modified(X)
print("Sorted using Modified Quick Sort:", quick_sorted_modified)
