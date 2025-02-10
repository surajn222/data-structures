# Pending
# implementation of quick sort in python using hoare partition scheme

def swap(a, b, arr):
    if a!=b:
        tmp = arr[a]
        arr[a] = arr[b]
        arr[b] = tmp

def quick_sort(arr, start, end):
    if start < end:
        pi = partition(arr, start, end)
        quick_sort(arr, start, pi-1)
        quick_sort(arr, pi+1, end)

def partition(arr, start_index, end_index):
    pivot_index = start_index
    pivot_value = arr[pivot_index]

    while start_index < end_index:
        while start_index < len(arr) and arr[start_index] <= pivot_value:
            start_index+=1
    
        while arr[end_index] > pivot_value:
            end_index-=1

        if start_index < end_index:
            swap(start_index, end_index, arr)

    swap(pivot_index, end_index, arr)

    return end_index


if __name__ == '__main__':
    arr = [11,9,29,7,2,15,28]
    # arr = ["mona", "dhaval", "aamir", "tina", "chang"]
    quick_sort(arr, 0, len(arr)-1)
    print(arr)

    tests = [
        [11,9,29,7,2,15,28],
        [3, 7, 9, 11],
        [25, 22, 21, 10],
        [29, 15, 28],
        [],
        [6]
    ]

    for arr in tests:
        quick_sort(arr, 0, len(arr)-1)
        print(f'sorted array: {arr}')

