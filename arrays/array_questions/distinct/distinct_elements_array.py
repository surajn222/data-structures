# python program to print all distinct elements in a given array

#Method 1

def printDistinct(arr, n):
    # Pick all elements one by one
    for index_array in range(0, n):

        # Check if the picked element is already printed
        element_already_exists = 0
        for index_check_in_array_so_far in range(0, index_array):
            if (arr[index_array] == arr[index_check_in_array_so_far]):
                element_already_exists = 1
                break

        # If not printed earlier, then print it
        if (element_already_exists == 0):
            print(arr[index_array])


# Driver program to test above function
arr = [6, 6,6, 10, 5, 4, 9, 120, 4, 6, 10]
length_array = len(arr)
printDistinct(arr, length_array)

# Time Complexity of above solution is O(n2).


#-----------------------------------------------------------
#Method 2
# Python program to print all distinct
# elements in a given array

def printDistinct(arr, n):
    # First sort the array so that
    # all occurrences become consecutive
    arr.sort(); #This can be done in O(nlogn)

    # Traverse the sorted array
    for i in range(n): #This can be done in n
        # Move the index ahead while there are duplicates
        if (i < n - 1 and arr[i] == arr[i + 1]):
            while (i < n - 1 and (arr[i] == arr[i + 1])):
                i += 1;
        # print last occurrence of the current element
        else:
            print(arr[i], end=" ");


# Driver code
arr = [6, 10, 5, 4, 9, 120, 4, 6, 10];
n = len(arr);
printDistinct(arr, n);
