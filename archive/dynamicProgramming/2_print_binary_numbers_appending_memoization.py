# Using 1, 2 , sum upto 3
# 111
# 21
# 12

arr = []
str_total = ""

rows, cols = (4, 4)
# dp = [[0]*cols]*rows
dp = [[0]*4 for _ in range(4)]

# print(dp[0][0])
#
# dp[0][0] = 1

print(dp)

# import sys
# sys.exit()

i = 0
j = 0
def print_numbers1(arr, str_total, i, j):
    # print(total)
    if len(str_total) >= 4:
        print("Stop ", str_total, i, j)
        # dp[i][j] = str_total
        # print(dp)
        return
    # total1 = total + 1

    # print(dp)
    str_total1 = str_total + str("0")
    # i = i + 0
    # i = i + 0
    print_numbers1(arr, str_total1, i, j)

    # total2 = total + 0
    str_total2 = str_total + str("1")

    # j = j + 1
    print_numbers1(arr, str_total2, i, j)


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
