# Define function
# first occurrence

def binary_search(array_1, low, high, target):
    if high >= low:   # Stop recursion
        mid = (low+high)//2
        if array_1[mid] == target:
            # If lower index value is less, then it is the first occurrence
            if array_1[mid-1]<target: return mid-1
            # If lower index value is same, then return binary search from low to lower index
            if array_1[mid-1] == target: return binary_search(array_1, low, mid-1, target)

            # If lower index value is less, then it is the first occurrence
            # if array_1[mid+1]>target: return mid+1
            # If lower index value is same, then return binary search from low to lower index
            # if array_1[mid+1] == target: return binary_search(array_1, mid+1, high, target)

        elif array_1[mid] > target: return binary_search(array_1, low, mid-1, target)
        elif array_1[mid] < target: return binary_search(array_1, mid+1, high, target)

# Define array
array_1 = [1,3,3,4,4,4,4,4,4,4,5,7,7,7,8,10,15,15,18,19]
target = 3
print("ceil of ", target)
print(binary_search(array_1, 0, len(array_1)-1, target))


