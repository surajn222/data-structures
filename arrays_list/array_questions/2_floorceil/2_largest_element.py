# Python program to find largest element
def largest_element_using_python_min_function(arr, length_of_array):
    maximum = max(arr)
    return maximum


def largest_element_using_sort_function(arr, length_of_array):
    arr = sorted(arr)
    return arr[-1]


def largest_element_using_traversal(arr, length_of_array):
    maximum = 0
    for i in arr:
        if i > maximum:
            maximum = i
    return maximum


# driver code
arr = [4,2,5,8,1,0]
length_of_array = len(arr)

print("original array")
print(arr)
print("modified array")
print(largest_element_using_python_min_function(arr, length_of_array))
print(largest_element_using_sort_function(arr, length_of_array))
print(largest_element_using_traversal(arr, length_of_array))




