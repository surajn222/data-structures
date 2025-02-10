# Step 1: Print all elements of the array in a while loop
# Step 2: Keep adding elements to a sub array
# Step 3: Remove elements from the sub array
# Step 4: Make the subarray the right size

def print_subarrays2(array_1):
	print(array_1)

	i = j = 0
	size_of_subarray = 3
	common_subarray = []

	while i <= len(array_1) - size_of_subarray:
		print(str(i) + " " + str(j))
		common_subarray.append(array_1[j])
		if j < size_of_subarray - 1:
			j += 1
			continue

		print("subarray size match: " + str(common_subarray))
		common_subarray.pop(0)
		i += 1
		j += 1


# Step 1: Print all elements of the array in a while loop
def step1(array_1):
	print("Step 1")
	i = 0
	while i <= len(array_1):
		print(i)
		i += 1

# Step 2: Keep adding elements to a sub array
def step2(array_1):
	print("Step 2")
	i = 0
	subarray = []
	while i <= len(array_1) - 1:
		print(i)
		subarray.append(array_1[i])
		i += 1

# Step 3: Remove elements from the sub array
def step3(array_1):
	print("Step 3")
	i = 0
	subarray = []
	while i <= len(array_1) - 1:
		print(i)
		subarray.append(array_1[i])
		print(subarray)
		subarray.pop()
		i += 1

# Step 4: Make the subarray the right size
def step4(array_1):
	print("Step 4")
	i = j = 0
	subarray = []
	k = 2
	while i <= len(array_1) - k - 1:
		print(j)
		subarray.append(array_1[j])

		if j < k - 1:
			j += 1
			continue

		print(subarray)
		subarray.pop(0)
		i += 1
		j += 1


def step5(array_1):
	print("Step 5 -----------------------")
	i = j = 0
	subarray = []
	k = 2
	map_count = {}
	while i <= len(array_1) - k - 1:
		print(j)
		subarray.append(array_1[j])

		map_count[array_1[j]] = map_count.get(array_1[j], 0) + 1

		if j < k - 1:
			j += 1
			continue

		if len(map_count) == k:
			print("Distinct: ")
		print(subarray)
		print(map_count)

		map_count[subarray[0]] = map_count.get(subarray[0], 0) - 1

		if map_count.get(subarray[0]) == 0:
			del map_count[subarray[0]]

		subarray.pop(0)

		i += 1
		j += 1


array_1 = [0, 1, 2, 3, 4, 5, 6, 8, 8, 8]

print_subarrays2(array_1)
print("-----------------")
step1(array_1)
step2(array_1)
step3(array_1)
step4(array_1)
step5(array_1)
