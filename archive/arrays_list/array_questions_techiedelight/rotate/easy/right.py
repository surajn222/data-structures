# Pending: Failed to implement this in leetcode
arr1 = [1, 2, 3, 4, 5, 6, 7]

rotate_by = 3
l = len(arr1)

arr1 = arr1 + arr1
print(arr1)

print("right rotate:")
print(arr1[rotate_by:(rotate_by + l)])

print("left rotate:")
print(arr1[l - rotate_by:(l - rotate_by + l)])
