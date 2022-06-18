import sys
from math import ceil
def search_arr(list_arr, search_element, min_index, max_index):
    # Binary Search
    # 1. Input: Array
    # 2. Search element
    # Operations
    # 1. Find the element at the middle of the array
    # 2. Check if the element at the mid is the search element
    # 3. If the middle element > search_element, get the first half of the array
    # 4. If the middle element < search_element, get the second half of the array
    # 5. Repeat

    print("min_index = " + str(min_index) + " max_index = " + str(max_index) + "\n")


    mid_index = int((max_index + min_index)/2)

    if search_element == list_arr[mid_index]:
        print("Element found = " + str(mid_index))
        return mid_index

    if list_arr[mid_index] > search_element:
        print("First half")
        search_arr(list_arr, search_element, min_index, mid_index-1)

    if list_arr[mid_index] < search_element:
        print("Second half")
        search_arr(list_arr, search_element, mid_index+1, max_index)


def insert_arr(list_arr, insert_element):
    # find the index of the element < insert_element

    list_arr.append(0)
    print("length = " + str(len(list_arr)))


    print("Array before")
    print(list_arr)

    i = 0
    while i < len(list_arr) - 1 and insert_element > list_arr[i]:
        print(i)
        i+=1


    for index_move_elements_from in range(len(list_arr)-1, i, -1):
        print("Index = " + str(index_move_elements_from))

        list_arr[index_move_elements_from] = list_arr[index_move_elements_from - 1]


    list_arr[i] = insert_element
    print("Array after")
    print(list_arr)

    sys.exit()

    # Insert the element


def delete_arr(list_arr):
    pass


# Driver function
list_arr = [10,20,30,40,50,60,70,80,90,100]
search_element = 60
#search_arr(list_arr, search_element, 0, len(list_arr)-1)
insert_arr(list_arr, 55)
delete_arr(list_arr)

