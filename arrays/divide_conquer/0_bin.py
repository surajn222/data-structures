def binary_search(arr, low, high, x):
    if high >= low:
        mid = (high + low)//2
        if arr[mid] == x: return mid
        elif arr[mid] < x: binary_search(arr, low, mid-1, x)
        else: binary_search(arr, mid+1, high, x)
    else:
        return -1

# Questions on binary search
# Binary Search to find X in sorted array: Basic binary search
# Implement Lower Bound: arr[x] >= given_value.
# - compare with higher and lower values
# Implement Upper Bound: arr[x] > given_value
# - compare with higher and lower values
# Search Insert Position: find where value will be inserted
# - compare with higher and lower values
# Floor/Ceil in Sorted Array: floor = max(all elements < given_value), ceil = min(all elements > given_value)
# - compare with higher and lower values
# Find the first or last occurrence of a given number in a sorted array
# - compare with higher and lower values
# Count occurrences of a number in a sorted array with duplicates
# - compare with higher and lower values
# Single element in a Sorted Array
# - compare with higher and lower values
# Find peak element
# - compare with higher and lower values
# Find square root of a number in log n:
# - brute force with binary search
# Find the Nth root of a number using binary search
# - brute force using binary search
# Split array - Largest Sum
# Median of 2 sorted arrays: https://www.youtube.com/watch?v=q6IEA26hvXc
# Kth element of 2 sorted arrays

# Search in Rotated Sorted Array I:
# - check for sorted side, make decision based on sorted side
# Search in Rotated Sorted Array II:
# - check for sorted side, make decision based on sorted side
# Find minimum in Rotated Sorted Array:
# - check for sorted side, make decision based on sorted side
# Find out how many times has an array been rotated:
# - check for sorted side, make decision based on sorted side

# Matrix
# Search in a 2 D matrix
# Search in a row and column wise sorted matrix
# Find Peak Element (2D Matrix)
# Matrix Median
# Find the row with maximum number of 1's

# Koko Eating Bananas: Problem
# Minimum days to make M bouquets: Problem
# Find the smallest Divisor: Problem
# Capacity to Ship Packages within D Days: Problem
# Kth Missing Positive Number: Problem
# Aggressive Cows: Problem
# Book Allocation Problem: Problem
# Painter's partition: Problem
# Minimize Max Distance to Gas Station: Problem