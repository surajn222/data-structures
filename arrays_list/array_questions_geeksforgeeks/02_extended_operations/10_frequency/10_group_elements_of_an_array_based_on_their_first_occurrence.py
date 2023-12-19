# TODO: Completed: Easy: Hashing
# Given an unsorted integer array containing many duplicate elements,
# rearrange it such that the same element appears together and the
# relative order of the first occurrence of each element remains unchanged

# The idea is to use hashing to solve this problem. Store the frequency of each element
# present in the input array in a map. Then traverse the input array, and for each element
# A[i], two cases are possible:
#
# If A[i] exists in the map, then this is the first occurrence of A[i] in the input array. Print the element, A[i], k times, where k is the frequency of A[i] in the input array (stored in the map). Finally, delete A[i] from the map to avoid getting reprocessed.
# If A[i] is not present on the map, then this is the repeated occurrence of A[i]. So move to the next element.


# Function to group elements of a given list based on the first
# occurrence of each element
def rearrange(A):
    # create an empty dictionary to store the frequency of each element
    # present in the input list
    freq = {}

    # traverse the input list and update the frequency of each element
    for i in A:
        freq[i] = freq.get(i, 0) + 1

    for i in A:
        # if `i` exists in the dictionary (first occurrence of `i`)
        if freq.get(i):
            # print `n` times, where `n = freq[i]`
            for _ in range(freq[i]):
                print(i, end=' ')

            # remove the element from the dictionary, so it would not
            # get processed again
            freq[i] = 0


if __name__ == '__main__':
    A = [5, 4, 5, 5, 3, 1, 2, 2, 4]
    rearrange(A)
