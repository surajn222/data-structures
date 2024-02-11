
dp = [[-1 for i in range(100)] for j in range(100)]

def step1(arr, len_arr, subset):
    print(f"Start {arr}, len_arr = {len_arr}, subset {subset}")

    if len_arr == 0:
        return

    subset1 = subset + str(arr[len_arr-1])
    new_len_arr1 = len_arr - 1
    step1(arr, new_len_arr1, subset1)

def step2(arr, len_arr, subset, sum_so_far, dp, length_of_subarray):
    print(f"Start {arr}, len_arr = {len_arr}, sum_so_far = {sum_so_far}, subset {subset}, len_of_subarray = {length_of_subarray}")

    if len_arr == 0:
        return

    if dp[len_arr][sum_so_far] != -1:
        print("returning the above")
        return dp[len_arr][sum_so_far]

    subset1 = subset + str(arr[len_arr-1])
    # new_len_arr1 = len_arr - 1
    # sum_subtract = sum_subtract - arr[len_arr-1]
    sum_so_far1 = sum_so_far + arr[len_arr-1]
    # dp[len_arr][sum_so_far1] = sum_so_far1
    length_of_subarray1 = length_of_subarray + 1
    dp[len_arr][sum_so_far1] = length_of_subarray1
    step2(arr, len_arr - 1, subset1, sum_so_far1, dp, length_of_subarray1)

    subset1 = subset
    sum_so_far2 = sum_so_far
    # dp[len_arr][sum_so_far2] = sum_so_far2
    length_of_subarray2 = length_of_subarray
    dp[len_arr][sum_so_far2] = length_of_subarray2
    step2(arr, len_arr - 1, subset1, sum_so_far2, dp, length_of_subarray2)

arr = [1,2,3,4,5,6,7]
len_arr = len(arr)
# print(step1(arr, len_arr, ""))
print(step2(arr, len_arr, "", 0, dp, 0))