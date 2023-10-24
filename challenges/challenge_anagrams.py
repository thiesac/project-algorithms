def is_anagram(first_string, second_string):
    first_list = list(first_string)
    second_list = list(second_string)

    merge_sort(first_list)
    merge_sort(second_list)

    return ''.join(first_list), ''.join(second_list)


def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        # initializes the variables i, j, and k to 0 simultaneously
        # i is the pointer for the left subarray.
        # j is the pointer for the right subarray.
        # k is the pointer for the merged array.
        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        # This loop ensures that any remaining elements in the left subarray
        # are added to the merged array.
        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        # This loop ensures that any remaining elements in the right subarray
        # are added to the merged array.
        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1


print(is_anagram("amor", "Roma"))
