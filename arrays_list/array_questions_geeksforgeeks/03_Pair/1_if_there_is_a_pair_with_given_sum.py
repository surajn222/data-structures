# Python 3 implementation of simple method to find count of pairs with given sum.

# Returns number of pairs in arr[0..n-1]
# with sum equal to 'sum'

# Find one pair/all pairs that sum/diff to a number
# Method 1:
# First element + (first, second, third, fourth)
# second element + (first, second, third, fourth)
# third element + (first, second, third, fourth)
# fourth element + (first, second, third, fourth)
# O(n^2)

# Method 2:
# Sum - first element of array(this is one part of the pair) = second part of the pair(count occurences of this number = add to a variable. this will happen twice)
# Sum - second element of array(this is one part of the pair) = second part of the pair(count occurences of this number = add to a variable. this will happen twice)
# Sum - third element of array(this is one part of the pair) = second part of the pair(count occurences of this number = add to a variable. this will happen twice)
# Sum - fourth element of array(this is one part of the pair) = second part of the pair(count occurences of this number = add to a variable. this will happen twice)
# O(n)

# Sum = first_element + second_element
# Sum - first_element = second_element
# Sum - first_element(loop) = second_element(count occurences in the array)

# Method 3:
# Find one pair
# Sort the array
# First element + (find an element that add to the "sum value" using binary search)


# Method 4:
# The simplest method is to run two loops, the outer loop picks the first element (smaller element) and the inner loop looks for the element picked by outer loop plus n. Time complexity of this method is O(n^2).
# We can use sorting and Binary Search to improve time complexity to O(nLogn). The first step is to sort the array in ascending order. Once the array is sorted, traverse the array from left to right, and for each element arr[i], binary search for arr[i] + n in arr[i+1..n-1]. If the element is found, return the pair.
# Both first and second steps take O(nLogn). So overall complexity is O(nLogn).
# The second step of the above algorithm can be improved to O(n). The first step remain same. The idea for second step is take two index variables i and j, initialize them as 0 and 1 respectively. Now run a linear loop. If arr[j] – arr[i] is smaller than n, we need to look for greater arr[j], so increment j. If arr[j] – arr[i] is greater than n, we need to look for greater arr[i], so increment i. Thanks to Aashish Barnwal for suggesting this approach. #PENDING

# https://leetcode.com/problems/finding-pairs-with-a-certain-sum/submissions/ #Pending


def getPairsCount_dict(arr, n, sum):

    dict_count_of_elements = {}

    # Store counts of all elements in map m
    for i in range(0, n):
        #print("Counting the elements in an array")
        if not arr[i] in dict_count_of_elements:
            dict_count_of_elements[arr[i]] = 1
        else:
            dict_count_of_elements[arr[i]] += 1

    twice_count = 0

    # Iterate through each element and increment
    # the count (Notice that every pair is
    # counted twice)
    list_pairs = []
    for i in range(0, n):

        #print("sum="+ str(sum))
        #print("arr element=" + str(arr[i]))
        #print("sum minus arr[i]=" + str(sum - arr[i]))
        #print("count of this element in the array = " + str(dict_count_of_elements[sum - arr[i]]))
        #print("count of this element in the array = " + str(dict_count_of_elements.get(sum - arr[i], 0)))
        twice_count += dict_count_of_elements.get(sum - arr[i], 0)
        if dict_count_of_elements.get(sum - arr[i], 0) != 0:
            list_pairs.append((arr[i], sum - arr[i]))
        #print("Twice count = " + str(twice_count))
        #print("\n")

        # if (arr[i], arr[i]) pair satisfies the
        # condition, then we need to ensure that
        # the count is  decreased by one such
        # that the (arr[i], arr[i]) pair is not
        # considered
        if (sum - arr[i] == arr[i]):
            twice_count -= 1

    # return the half of twice_count
    print(list_pairs)
    print("twice count" + str(twice_count))
    return int(twice_count / 2)



def getPairsCount_arr(arr, n, sum):

    count_of_elements = [0] * n

    # Store counts of all elements in map m
    for i in range(0, n):
        #print("Counting the elements in an array")
        count_of_elements[arr[i]] += 1

    #print(count_of_elements)

    twice_count = 0

    # Iterate through each element and increment
    # the count (Notice that every pair is
    # counted twice)
    for i in range(0, n):

        #print("sum="+ str(sum))
        #print("arr element=" + str(arr[i]))
        #print("sum minus arr[i]=" + str(sum - arr[i]))
        #print("count of this element in the array = " + str(count_of_elements[sum - arr[i]]))
        twice_count += count_of_elements[sum - arr[i]]
        #print("Twice count = " + str(twice_count))
        #print("\n")

        # if (arr[i], arr[i]) pair satisfies the
        # condition, then we need to ensure that
        # the count is  decreased by one such
        # that the (arr[i], arr[i]) pair is not
        # considered
        if (sum - arr[i] == arr[i]):
            twice_count -= 1

    # return the half of twice_count
    return int(twice_count / 2)




def getPairsCountTwoLoops(arr, n, sum):

    # Store counts of all elements in map m
    set_pairs = set()
    list_pairs = []
    for index_outer_loop in range(0, n-1):
        for index_inner_loop in range(index_outer_loop, n):
            if arr[index_outer_loop] + arr[index_inner_loop] == sum:
                tup = (arr[index_outer_loop], arr[index_inner_loop])
                list_pairs.append(tup)

    print(list_pairs)
    print(len(list_pairs))
    return len(list_pairs)





def getPairsCountSortTraverseDiff(arr, n, sum):
    arr.sort()
    print(arr)


    i, j = 0, 1


    while i < n and j < n:
        if i != j and arr[j]+arr[i] == sum:
            print("Pair found (",arr[i],",",arr[j],")")
            i+=1
            j+=1
        elif arr[j] + arr[i] > sum:
            print(str(arr[j]) + " + " + str(arr[i]) + " < " + str(sum) + "\n")
            j+=1
        else:
            print(str(arr[j]) + " + " + str(arr[i]) + " > " + str(sum) + "\n")
            i+=1
    #print("No pair found")
    return False


def getPairsCountSortTraverseSum(arr, n, sum):
    arr.sort()
    print(arr)


    i, j = 0, n - 1


    while i < j:
        if i != j and arr[j]+arr[i] == sum:
            print("Pair found (",arr[i],",",arr[j],")")
            i+=1
            j+=1
        elif arr[j] + arr[i] > sum:
            print(str(arr[j]) + " + " + str(arr[i]) + " < " + str(sum) + "\n")
            j-=1
        else:
            print(str(arr[j]) + " + " + str(arr[i]) + " > " + str(sum) + "\n")
            i+=1
    #print("No pair found")
    return False


# Driver function
import random
arr = []
for i in range(0, 10):
    arr.append(random.randint(0,10))
n = len(arr)
print("Array ")
print(arr)
print(n)
sum = 6

print('\n')

# Method 4
import timeit
start = timeit.default_timer()
print("Count of pairs Sort is", getPairsCountSortTraverseSum(arr,n, sum))
stop = timeit.default_timer()
print('Time two loops: ', stop - start)
print("\n")

import sys
sys.exit()


# Method 1
import timeit
start = timeit.default_timer()
print("Count of pairs two loops is", getPairsCountTwoLoops(arr,n, sum))
stop = timeit.default_timer()
print('Time two loops: ', stop - start)
print("\n")

#Method 2
import timeit
start = timeit.default_timer()
print("Count of pairs dict is", getPairsCount_dict(arr,n, sum))
stop = timeit.default_timer()
print('Time dict: ', stop - start)
print("\n")

# Method 2
start = timeit.default_timer()
print("Count of pairs arr is", getPairsCount_arr(arr,n, sum))
stop = timeit.default_timer()
print('Time arr: ', stop - start)
print("\n")

# Method 3
# Pending

import sys
sys.exit()

# Driver function
arr = [1, 5, 10, -10, 50]
n = len(arr)
sum = 6

print("Count of pairs is", getPairsCount(arr,n,sum))
