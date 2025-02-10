def merge(nums1, m: int, nums2, n: int) -> None:
	"""
	Do not return anything, modify nums1 in-place instead.
	"""
	arr1 = nums1
	arr2 = nums2
	nums1 = [0] * (len(arr1) + len(arr2))
	k = i = j = 0
	while i < m and j < n:
		print("i: " + str(i))
		print("j: " + str(j))
		if arr1[i] <= arr2[j]:
			print("adding " + str(i) + " to " + str(k))
			nums1[k] = arr1[i]
			i = i + 1
		else:
			nums1[i] = arr2[j]
			j = j + 1
		k = k + 1
		print(nums1)

	print("here1")
	while i < len(arr1):
		nums1[k] = arr1[i]
		i = i + 1
		k = k + 1
	print("here1")
	while j < len(arr2):
		nums1[k] = arr2[j]
		j = j + 1
		k = k + 1

	print(nums1)


list1 = [1, 2, 3]
list2 = [2, 5, 6]

merge(list1, len(list1), list2, len(list2))
