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

def print_numbers3(arr, index, val, target_arr):
    if index == 2:
        print("Stop and return", index)
        if val == 0:
            return []
        else:
            return [target_arr[index]]
    if index > 3:
        return 0

    new_index = index + 1
    # Do not include
    arr_temp1 = print_numbers3([], new_index, 0, target_arr)
    print("returned " + str(arr_temp1))

    arr.append(target_arr[index])
    for i in arr_temp1:
        arr.append(str(target_arr[index])+str(i))
    # arr.append(target_arr[index])
    arr.extend(arr_temp1)
    # new_index = index + 1
    # Yes include
    arr_temp2 = print_numbers3([], new_index, 1, target_arr)
    print("returned " + str(arr_temp2))
    arr.append(target_arr[index])
    for i in arr_temp2:
        arr.append(str(target_arr[index])+str(i))

    arr.extend(arr_temp2)

    # print("return val = ", str(val)+val1+val2)
    return arr

def print_numbers4(arr, index):
    if index == 3:
        print("Stop and return", index)
        return arr[index]
    else:
        return 0



arr = []
target_arr = [1,2,3]
print(print_numbers3(arr, 0, "", target_arr))
