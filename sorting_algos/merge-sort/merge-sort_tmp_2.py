# Step 1: split array into left array and right array.
# Step 2:
# Step 3:

def merge_sort(unsorted_array):
    if len(unsorted_array) == 1:
        return
    mid_element = len(unsorted_array) // 2

    left_array = unsorted_array[mid_element:]
    right_array = unsorted_array[:mid_element]

    merge_sort(left_array)
    merge_sort(right_array)

    merge_two_sorted_lists(left_array, right_array, unsorted_array)


def merge_sort_test(unsorted_array):
    if len(unsorted_array) == 1:
        return
    mid_element = len(unsorted_array) // 2

    left_array = unsorted_array[mid_element:]
    right_array = unsorted_array[:mid_element]

    merge_sort(left_array)
    merge_sort(right_array)

    merge_two_sorted_lists(left_array, right_array, unsorted_array)


# Step 2: Visualize this divide and conquer algorithm
def merge_sort_1(unsorted_array):
    unsorted_left_array_will_return_sorted = unsorted_array[0]
    unsorted_right_array_will_return_sorted = unsorted_array[1]
    merge_two_sorted_lists(unsorted_left_array_will_return_sorted, unsorted_right_array_will_return_sorted, [None] * (
                len(unsorted_left_array_will_return_sorted) + len(unsorted_right_array_will_return_sorted)))


# Step 2: Visualize this divide and conquer algorithm
def merge_sort_2(unsorted_array):
    print("2 Mergesort called with array: " + str(unsorted_array))
    if len(unsorted_array) <= 1:
        print("Return Mergesort called with array: " + str(unsorted_array))
        return

    mid_element = len(unsorted_array) // 2

    unsorted_left_array_will_return_sorted = unsorted_array[:mid_element]
    unsorted_right_array_will_return_sorted = unsorted_array[mid_element:]

    print("2 ---Left array before merge: " + str(unsorted_left_array_will_return_sorted))
    print("2 ---Right array before merge: " + str(unsorted_right_array_will_return_sorted))

    merge_sort_3(unsorted_left_array_will_return_sorted)
    merge_sort_3(unsorted_right_array_will_return_sorted)

    print("2 ---Left array after merge: " + str(unsorted_left_array_will_return_sorted))
    print("2 ---Right array after merge: " + str(unsorted_right_array_will_return_sorted))
    merge_two_sorted_lists(unsorted_left_array_will_return_sorted, unsorted_right_array_will_return_sorted,
                           unsorted_array)


# Step 2: Visualize this divide and conquer algorithm
def merge_sort_3(unsorted_array):
    print("3 Mergesort called with array: " + str(unsorted_array))
    if len(unsorted_array) <= 1:
        print("Return Mergesort called with array: " + str(unsorted_array))
        return

    mid_element = len(unsorted_array) // 2

    unsorted_left_array_will_return_sorted = unsorted_array[:mid_element]
    unsorted_right_array_will_return_sorted = unsorted_array[mid_element:]

    print("3 ---Left array before merge: " + str(unsorted_left_array_will_return_sorted))
    print("3 ---Right array before merge: " + str(unsorted_right_array_will_return_sorted))

    merge_sort_4(unsorted_left_array_will_return_sorted)
    merge_sort_4(unsorted_right_array_will_return_sorted)

    print("3 ---Left array after merge: " + str(unsorted_left_array_will_return_sorted))
    print("3 ---Right array after merge: " + str(unsorted_right_array_will_return_sorted))
    merge_two_sorted_lists(unsorted_left_array_will_return_sorted, unsorted_right_array_will_return_sorted,
                           unsorted_array)


# Step 2: Visualize this divide and conquer algorithm
def merge_sort_4(unsorted_array):
    print("4 Mergesort called with array: " + str(unsorted_array))
    if len(unsorted_array) <= 1:
        print("4 Return Mergesort called with array: " + str(unsorted_array))
        return

    mid_element = len(unsorted_array) // 2

    unsorted_left_array_will_return_sorted = unsorted_array[:mid_element]
    unsorted_right_array_will_return_sorted = unsorted_array[mid_element:]

    print("4 ---Left array before merge: " + str(unsorted_left_array_will_return_sorted))
    print("4 ---Right array before merge: " + str(unsorted_right_array_will_return_sorted))

    merge_sort_4(unsorted_left_array_will_return_sorted)
    merge_sort_4(unsorted_right_array_will_return_sorted)

    print("4 ---Left array after merge: " + str(unsorted_left_array_will_return_sorted))
    print("4 ---Right array after merge: " + str(unsorted_right_array_will_return_sorted))
    merge_two_sorted_lists(unsorted_left_array_will_return_sorted, unsorted_right_array_will_return_sorted,
                           unsorted_array)


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
        merge_sort_test(unsorted_array)
        # print(unsorted_array)

    # arr = [0,0,0,0,0,0,0,0]
    # arr1 = [1,3,5,7]
    # arr2 = [2,4,6,8]
    # merge_two_sorted_lists(arr1,arr2, arr)
    # print(arr)
