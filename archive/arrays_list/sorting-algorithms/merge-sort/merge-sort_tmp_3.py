# Step 1: split array into left array and right array.
# Step 2:
# Step 3:

def merge_sort(unsorted_array):
    # 1. Check if the array is sorted? Return (Single element = Sorted)
    # 2. If yes, go for merge.
    # 3. If not, we have to sort it. How? Split till single element. (sorted array)

    if len(unsorted_array) == 1:
        return

    mid_element = len(unsorted_array) // 2
    left_array = unsorted_array[:mid_element]
    right_array = unsorted_array[mid_element:]

    merge_sort(left_array)
    merge_sort(right_array)

    merge_two_sorted_lists(left_array, right_array, unsorted_array)


# Step 1: Learn how to merge two lists
def merge_two_sorted_lists(unmerged_array_1, unmerged_array_2, merged_array):  # Do this visually
    print("Arrays to merge: " + str(unmerged_array_1) + " " + str(unmerged_array_2) + " " + str(merged_array))
    len_unmerged_array_1 = len(unmerged_array_1)
    len_unmerged_array_2 = len(unmerged_array_2)

    unmerged_array_1_index = unmerged_array_2_index = merged_array_index = 0

    while unmerged_array_1_index < len_unmerged_array_1 and unmerged_array_2_index < len_unmerged_array_2:
        if unmerged_array_1[unmerged_array_1_index] <= unmerged_array_2[unmerged_array_2_index]:
            merged_array[merged_array_index] = unmerged_array_1[unmerged_array_1_index]
            unmerged_array_1_index += 1
        else:
            merged_array[merged_array_index] = unmerged_array_2[unmerged_array_2_index]
            unmerged_array_2_index += 1
        merged_array_index += 1

    while unmerged_array_1_index < len_unmerged_array_1:
        merged_array[merged_array_index] = unmerged_array_1[unmerged_array_1_index]
        unmerged_array_1_index += 1
        merged_array_index += 1

    while unmerged_array_2_index < len_unmerged_array_2:
        merged_array[merged_array_index] = unmerged_array_2[unmerged_array_2_index]
        unmerged_array_2_index += 1
        merged_array_index += 1

    print("Arrays merged: " + str(unmerged_array_1) + " " + str(unmerged_array_2) + " " + str(merged_array))


if __name__ == '__main__':
    test_cases = [
        [[1, 3, 15], [2, 8, 9]],
        [[3, 10], [7, 8]],
        [[10], [7]]
    ]

    test_cases = [
        [8, 2, 16, 54, 3, 1]
    ]

    for unsorted_array in test_cases:
        print("------------------------------------------")
        merge_sort(unsorted_array)
        # print(unsorted_array)

    # arr = [0,0,0,0,0,0,0,0]
    # arr1 = [1,3,5,7]
    # arr2 = [2,4,6,8]
    # merge_two_sorted_lists(arr1,arr2, arr)
    # print(arr)
