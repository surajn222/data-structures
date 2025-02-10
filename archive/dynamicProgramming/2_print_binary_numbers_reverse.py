# Using 1, 2 , sum upto 3
# 111
# 21
# 12

arr = []
str_total = ""
def print_numbers1(arr, str_total, val_here, count):
    print("count, val_here", count, val_here)
    # if len(str_total) >= 4:
    if count >= 3:
        # print("Stop ", val_here)
        return val_here
    # total1 = total + 1
    # str_total1 = str_total + str("0")
    # new_val1 = int(val_here) + 0
    str_total1 = str_total2 = ""
    count += 1
    val_here1 = print_numbers1(arr, str_total1, 0, count)
    print("return val_here1 = " + str(val_here1))
    # total2 = total + 0
    # str_total2 = str_total + str("1")
    # new_val2 = int(val_here) + 1
    val_here2 = print_numbers1(arr, str_total2, 1, count)
    print("return val_here2 = " + str(val_here2))

    final_val = str(val_here) + str(val_here1) + str(val_here2)
    print("---- final_val", final_val)
    return final_val

def print_numbers2(total, arr, str_total):
    print(total)

    if total == 3:
        if total == 3:
            print("Stop ", str_total)
        return

    total1 = total + 1
    str_total1 = str_total +str("1")
    print_numbers3(total1, arr, str_total1)
    total2 = total + 2
    str_total2 = str_total + str("2")
    print_numbers3(total2, arr, str_total2)

def print_numbers3(total, arr, str_total):
    print(total)

    if total >= 3:
        if total == 3:
            print("Stop ", str_total)
        return

    total1 = total + 1
    str_total1 = str_total + str("1")
    print_numbers4(total1, arr, str_total1)
    total2 = total + 2
    str_total2 = str_total + str("2")
    print_numbers4(total2, arr, str_total2)

def print_numbers4(total, arr, str_total):
    if total >= 3:
        if total == 3:
            print("Stop ", str_total)
        # print(str_total)
        return

print_numbers1(arr, str_total, 0, 0)
