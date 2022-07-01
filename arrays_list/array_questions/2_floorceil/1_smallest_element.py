def smallest_element_using_python_min_function(arr, length_of_array):
    minimum = min(arr)
    return minimum


def smallest_element_using_sort_function(arr, length_of_array):
    arr = sorted(arr)
    return arr[0]


def smallest_element_using_traversal(arr, length_of_array):
    minimum = 999999
    for i in arr:
        if i < minimum:
            minimum = i
    return minimum


# driver code
arr = [4,2,5,8,1]
length_of_array = len(arr)

print("original array")
print(arr)
print("modified array")
print(smallest_element_using_python_min_function(arr, length_of_array))
print(smallest_element_using_sort_function(arr, length_of_array))
print(smallest_element_using_traversal(arr, length_of_array))



