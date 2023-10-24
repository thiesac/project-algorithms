def is_anagram(first_string, second_string):
    first_list = list(first_string.lower())
    second_list = list(second_string.lower())

    first_sorted = merge_sort(first_list)
    second_sorted = merge_sort(second_list)

    return "".join(first_sorted), "".join(second_sorted)


def merge(left_half, right_half):
    merged = []
    # initializes the variables i and j to 0 simultaneously
    # i is the pointer for the left subarray.
    # j is the pointer for the right subarray.
    i = j = 0

    while i < len(left_half) and j < len(right_half):
        if left_half[i] < right_half[j]:
            merged.append(left_half[i])
            i += 1
        else:
            merged.append(right_half[j])
            j += 1

        # This loop ensures that any remaining elements in the left subarray
        # are added to the merged array.
    while i < len(left_half):
        merged.append(left_half[i])
        i += 1

        # This loop ensures that any remaining elements in the right subarray
        # are added to the merged array.
    while j < len(right_half):
        merged.append(right_half[j])
        j += 1

    return merged


def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left_half = merge_sort(arr[:mid])
    right_half = merge_sort(arr[mid:])

    return merge(left_half, right_half)


print(is_anagram("amor", "Roma"))
