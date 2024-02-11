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

def print_numbers3(arr, index, target_arr):
    print("TG", str(target_arr), index)
    if len(target_arr) == 1:
        print("Stop and return", index)
        if target_arr:
            return target_arr[0]
        else:
            return 0
    if len(target_arr) == 0:
        return
        # if val == 0:
        #     return []
        # else:
        #     return [target_arr[index]]

    # new_index = index + 1
    # Do not include
    # len_arr = len(target_arr)
    arr_val1 = print_numbers3([], index, target_arr[1:])
    print("returned " + str(arr_val1))
    # arr.extend(arr_temp1)
    # for i in arr_temp1:
    #     arr.append(str(target_arr[index])+str(i))
    # # arr.append(target_arr[index])
    # arr.extend(arr_temp1)
    # new_index = index + 1
    # Yes include
    arr_val2 = print_numbers3([], index, target_arr[2:])
    if arr_val2 is not None:
        print("returned " + str(arr_val2))
    else:
        arr_val2 = 0
    # arr.extend(target_arr)
    # for i in arr_temp2:
    #     arr.append(str(target_arr[index])+str(i))
    #
    # arr.extend(arr_temp2)
    if arr_val1 + arr_val2 == 3:
        print("Found ", arr_val1, arr_val2, "-------")

    # print("return val = ", str(val)+val1+val2)
    return arr_val1 + arr_val2

def print_numbers4(arr, index):
    if index == 3:
        print("Stop and return", index)
        return arr[index]
    else:
        return 0



arr = []
target_arr = [1,2,3,4]
print(print_numbers3(arr, 0, target_arr))
