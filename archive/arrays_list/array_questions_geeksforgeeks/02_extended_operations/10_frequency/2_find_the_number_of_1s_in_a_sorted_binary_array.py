# TODO
# Given a binary array arr[] of size N, which is sorted in non-increasing order, count the number of 1’s in it.

# Sol1: A simple solution is to linearly traverse the array until we find the 1’s in the array and keep count of 1s. If the array element becomes 0 then return the count of 1’s.

# Sol2: We can use Binary Search to find count in O(Logn) time. The idea is to look for the last occurrence of 1 using Binary Search. Once we find the index’s last occurrence, we return index + 1 as count.