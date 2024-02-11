# Using 1, 2 , sum upto 3
# 111
# 21
# 12

arr = []
str_total = ""
def print_numbers1(total, arr, str_total):
    print(total)
    if total >= 3:
        if total == 3:
            print("Stop ", str_total)
        return
    total1 = total + 1
    str_total1 = str_total + str("1")
    print_numbers1(total1, arr, str_total1)
    total2 = total + 2
    str_total2 = str_total + str("2")
    print_numbers1(total2, arr, str_total2)

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

print_numbers1(0, arr, str_total)
