
def minimumElement(arr, arr_size):
    min = arr[0]
    for index_traverse_array in range(1, arr_size):
        if arr[index_traverse_array] < min:
            min = arr[index_traverse_array]

    print(min)

# Driver code
arr = [4, 2, 4, 5, 2, 3, 1]
arr_size = len(arr)
minimumElement(arr, arr_size)