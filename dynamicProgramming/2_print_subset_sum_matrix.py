# Using 1, 2 , sum upto 3
# 111
# 21
# 12

arr = [1,2,3,4,5,6]
str_total = ""

rows, cols = (4, 4)
dp = [[-1]*6 for _ in range(6)]

print(dp)

def print_numbers1(arr, sub_arr, count):
    # print(total)
    # if len(str_total) >= 4:
    #     print("Stop ", str_total)
    #     return
    # else:
    # print("arr: ", arr)

    sub_arr1 = sub_arr.copy()
    sub_arr2 = sub_arr.copy()


    if len(arr) > 0:
        sub_arr1.append(arr[0])
        count = count + 1
        # if sum(sub_arr1) == 6:
        #     print("SUM found: ", sub_arr1)
        # if sum(sub_arr2) == 6:
        #     print("SUM found: ", sub_arr2)
        str1 = '\n' + " "*count + "subarr1", sub_arr1, " length = ", len(sub_arr1), " rec_count = ", count
        print(str1)

        if sub_arr1:
            if len(sub_arr1) == 1:
                i = 0
                j = sub_arr1[-1]-1
            elif len(sub_arr1) > 1:
                i = sub_arr1[-2]-1
                j = sub_arr1[-1]-1
            print("i = ", i, " j = ", j)
            if dp[i][j] == -1:
                # return
                dp[i][j] = str(sub_arr1)

        # else:
        #     print("Matrix full")
        print(dp)

        str2 = '\n' + " "*count + "subarr2", sub_arr2, " length = ", len(sub_arr2), " rec_count = ", count
        print(str2)
        if sub_arr2:
            if len(sub_arr2) == 1:
                i = 0
                j = sub_arr2[0]-1
            elif len(sub_arr2) > 1:
                i = sub_arr2[-2]-1
                j = sub_arr2[-1]-1
            print("i = ", i, " j = ", j)
            if dp[i][j] == -1:
                # return
                dp[i][j] = str(sub_arr2)
        # else:
        #     print("Matrix full")
        print(dp)
    else:
        return

    # sub_arr2
    print_numbers1(arr[1:], sub_arr1, count)
    print_numbers1(arr[1:], sub_arr2, count)


def print_numbers2(total, arr, str_total):
    print(total)

    if total == 3:
        if total == 3:
            print("Stop ", str_total)
        return

    total1 = total + 1
    str_total1 = str_total + str("1")
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

print_numbers1(arr, [], count=0)
