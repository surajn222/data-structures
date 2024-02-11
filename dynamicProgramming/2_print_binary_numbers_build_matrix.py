# Using 1, 2 , sum upto 3
# 111
# 21
# 12

arr = []
str_total = ""

rows, cols = (4, 4)
dp = [[-1]*3 for _ in range(3)]

print(dp)

i = 0
j = 0
def print_numbers1(arr, i, j):
    print("called print_numbers1")
    if j == 3 or i == 3:
        print("Stop")
        return

    print(i, j)
    if dp[i][j] != -1:
        print("Returning due to value already set")
        return

    dp[i][j] = str(i) + " "  + str(j)
    print(dp)
    print_numbers1(arr, i+1, j)
    print_numbers1(arr, i, j+1)

def print_numbers2(arr, i, j):
    print("called print_numbers2")

    # j = j + 1

    print(i, j)
    print_numbers2(arr, i, j+1)
    # print(j)
    # if i == 2:
    #     print("Stop")
    #     return
    # i = i + 1
    print_numbers2(arr, i+1, j)


def print_numbers3(arr, i, j):
    if i == 4:
        print("Stop")
        return


def print_numbers4(arr, i, j):
    print(i, j)
    i = i + 1
    print_numbers5(arr, i, j)
    # print(j)
    j = j + 1
    print_numbers5(arr, i, j)


def print_numbers5(arr, i, j):
    if i == 4:
        print("Stop")
        return

print_numbers1(dp, 0, 0)
