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

def print_numbers3(arr, var_len, final_len):
    # print("var_len ", var_len)
    if var_len <= 0:
        print("len_arr is 0 = ", var_len)
        if var_len >= 0:
            return arr[final_len-var_len-1]
        else:
            return None

    new_len = var_len - 1
    val1 = print_numbers3(arr, new_len, final_len)
    if val1 is not None:
        print(f"Matrix1 = j = ", str(var_len-1) + " number, i = ", str(arr[final_len-var_len]), " val1 = ", val1)
    else:
        val1 = 0

    new_len = var_len - 2
    val2 = print_numbers3(arr, new_len, final_len)
    if val2 is not None:
        print(f"Matrix2 = j = ", str(var_len-1) + " number, i = ", str(arr[final_len-var_len]), " val2 = ", val2)
    else:
        val2 = 0
    return val1 + val2

def print_numbers4(arr, index):
    if index == 3:
        print("Stop and return", index)
        return arr[index]
    else:
        return 0



arr = []
target_arr = [1,2,3,4]
final_len = len(target_arr)
print(print_numbers3(target_arr, final_len, final_len))


