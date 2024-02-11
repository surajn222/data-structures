
dp = [[-1 for i in range(16)] for j in range(16)]

def step1(arr, len_arr, subset):
    print(f"Start {arr}, len_arr = {len_arr}, subset {subset}")

    if len_arr == 0:
        return

    subset1 = subset + str(arr[len_arr-1])
    new_len_arr1 = len_arr - 1
    step1(arr, new_len_arr1, subset1)

def step2(arr, len_arr, subset, sum_so_far, length_of_subarray, total_count):
    print(f"Start {arr}, len_arr = {len_arr}, sum_so_far = {sum_so_far}, subset {subset}, len_of_subarray = {length_of_subarray}")

    if sum_so_far == 6:
        # Add to dp
        total_count = total_count + 1
        print(f"Added upto 7 =============== ^, total_count = {total_count}")

        return total_count

    if dp[len_arr-1][sum_so_far] != -1:
        print("returning the above")
        return dp[len_arr-1][sum_so_far]

    if len_arr == 0:
        print("returning, len_arr is 0")
        return 0


    subset1 = subset + str(arr[len_arr-1])
    # new_len_arr1 = len_arr - 1
    # sum_subtract = sum_subtract - arr[len_arr-1]
    sum_so_far1 = sum_so_far + arr[len_arr-1]
    # dp[len_arr][sum_so_far1] = sum_so_far1
    length_of_subarray1 = length_of_subarray + 1
    # if sum_so_far1 == 7:
    #     # Add to dp
    #     total_count1 = total_count + 1
    # else:
    #     total_count1 = total_count

    total_count1 = step2(arr, len_arr - 1, subset1, sum_so_far1, length_of_subarray1, total_count)
    print(f"Adding {total_count1} to dp at {len_arr-1}, {sum_so_far1}")
    dp[len_arr-1][sum_so_far1] = total_count1

    subset2 = subset
    sum_so_far2 = sum_so_far
    # dp[len_arr][sum_so_far2] = sum_so_far2
    length_of_subarray2 = length_of_subarray
    # if sum_so_far2 == 7:
    #     # Add to dp
    #     total_count2 = total_count + 1
    # else:
    #     total_count2 = total_count

    total_count2 = step2(arr, len_arr - 1, subset2, sum_so_far2, length_of_subarray2, total_count)
    dp[len_arr-1][sum_so_far2] = total_count2



    # subset3 = subset
    # sum_so_far3 = sum_so_far
    # # dp[len_arr][sum_so_far2] = sum_so_far2
    # length_of_subarray3 = length_of_subarray
    # # if sum_so_far2 == 7:
    # #     # Add to dp
    # #     total_count2 = total_count + 1
    # # else:
    # #     total_count2 = total_count
    #
    # total_count3 = step2(arr, len_arr - 1, subset3, sum_so_far3, length_of_subarray3, total_count)
    # dp[len_arr-1][sum_so_far3] = total_count3



    if total_count1 == None:
        total_count1 = 0
    if total_count2 == None:
        total_count2 = 0
    return total_count1 + total_count2

arr = [1,2,3,4,5]
# Count the subarrays that add upto 7
len_arr = len(arr)
# print(step1(arr, len_arr, ""))
print(step2(arr, len_arr, "", 0, 0, 0))