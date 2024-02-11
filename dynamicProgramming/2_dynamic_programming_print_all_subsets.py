



def print_numbers1(arr, count):
    print("Before " + "count " + str(count))
    if len(arr) == count:
        return

    c = count+1
    print_numbers2(arr, c)
    print("After " + "count " + str(count) + " arr_val " + str(arr[count]))

    c = count + 0
    # arr = arr[count]
    print_numbers2(arr, c)
    print("After " + "count " + str(count) + " arr_val " + str(arr[count]))


def print_numbers2(arr, count):
    print("Before " + "count " + str(count))
    if len(arr) == count:
        return

    c = count+1
    print_numbers3(arr, c)
    print("After " + "count " + str(count) + " arr_val " + str(arr[count]))

    # c = count + 0
    arr = arr[count]
    print_numbers3(arr, c)
    print("After " + "count " + str(count) + " arr_val " + str(arr[count]))

def print_numbers3(arr, count):
    print("Before " + "count " + str(count))
    if len(arr) <= count:
        return

    c = count+1
    print_numbers3(arr, c)
    print("After " + "count " + str(count) + " arr_val1 " + str(arr[count]))

    c = count + 0
    # arr = arr[count]
    print_numbers3(arr, c)
    print("After " + "count " + str(count) + " arr_val " + str(arr[count]))


arr = [1, 2, 3, 4, 5]
print_numbers1(arr, count=0)
