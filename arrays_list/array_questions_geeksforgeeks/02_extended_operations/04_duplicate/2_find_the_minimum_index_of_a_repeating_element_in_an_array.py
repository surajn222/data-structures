# Sol1:
# Two loops

# Sol2:
# Sort and traverse

# Sol3:
# Traverse from right to left, use hashmap to store elements, if duplicate is found, that is the repeating element to most left

def printFirstRepeating(arr, n):
    dict_dup = {}
    rep_element = -1
    for i in range(n-1,-1, -1):
        print(arr[i])
        if arr[i] in dict_dup:
            rep_element = arr[i]
        else:
            dict_dup[arr[i]] = dict_dup.get(arr[i], 0) + 1
        print(dict_dup)
    return rep_element

# Driver Code
arr = [10, 6, 3, 4, 3, 5, 6]

n = len(arr)
print(printFirstRepeating(arr, n))