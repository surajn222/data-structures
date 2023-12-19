# Using 1, 2 , sum upto 3
# 111
# 21
# 12

arr = []
str_total = ""
def print_numbers1(arr, index):
    new_index = index + 1
    return_val = print_numbers2(arr, new_index)
    print(str(return_val)  + str(arr[index]))
    val = str(return_val) + str(arr[index])
    return val

def print_numbers2(arr, index):
    new_index = index + 1
    return_val = print_numbers3(arr, new_index)
    print(str(return_val)  + str(arr[index]))
    val = str(return_val) + str(arr[index])
    return val

def print_numbers3(arr, index, val):
    if index == 4:
        print("Stop and return", val)
        return [val]
    if index > 3:
        return 0

    val = str(val)
    new_index = index + 1
    arr_temp1 = print_numbers3([], new_index, 0)
    print("returned " + str(arr_temp1))

    for i in arr_temp1:
        arr.append(str(val)+str(i))

    # new_index = index + 1
    arr_temp2 = print_numbers3([], new_index, 1)
    print("returned " + str(arr_temp2))
    for i in arr_temp2:
        arr.append(str(val)+str(i))

    # print("return val = ", str(val)+val1+val2)
    return arr

def print_numbers4(arr, index):
    if index == 3:
        print("Stop and return", index)
        return arr[index]
    else:
        return 0



arr = []
print(print_numbers3(arr, 0, ""))
