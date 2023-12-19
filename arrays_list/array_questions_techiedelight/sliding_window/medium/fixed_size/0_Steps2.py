# Step 1: Print all elements of the array in a while loop
# Step 2: Keep adding elements to a sub array
# Step 3: Add elements upto k and stop
# Step 4: Add the last element, remove the first element


# Step 1: Print all elements of the array in a while loop
def step1(array_1):
	print("Step 1: Print all elements of the array in a while loop")
	i = 0
	while i <= len(array_1):
		print(i)
		i += 1

# Step 2: Keep adding elements to a sub array
def step2(array_1):
	print("Step 2: Keep adding elements to a sub array")
	i = 0
	subarray = []
	while i <= len(array_1) - 1:
		print(i)
		subarray.append(array_1[i])
		print(subarray)
		i += 1

# Step 3: Add elements upto k
def step3(array_1):
	print("Step 3")
	i = 0
	subarray = []
	k = 3
	while i <= len(array_1) - 1:
		print(i)
		subarray.append(array_1[i])
		print(subarray)
		if i < k - 1:
			i += 1
			continue
		else:
			break

# Step 4: Introduce j for the smaller subarray, j = len(subarray)
def step4(array_1):
	print("Introduce len_subarray variable which is separate than i")
	i = 0
	len_subarray = 0
	subarray = []
	k = 3
	while i <= len(array_1) - 1:
		print(i)
		subarray.append(array_1[i])
		print(subarray)
		if len_subarray < k - 1:
			i += 1
			len_subarray += 1
			continue
		break

# When we reach 3 elements, remove first element, and let the loop run
def step5(array_1):
	print("When we reach 3 elements, remove first element, and let the loop run")
	i = len_subarray = 0
	subarray = []
	k = 3
	while i <= len(array_1) - 1:
		print(i)
		subarray.append(array_1[i])

		if len_subarray < k - 1:
			i += 1
			len_subarray += 1
			continue

		print(subarray)
		subarray.pop(0)
		i += 1





def step6(array_1):
	print("Step 3")
	i = j = 0
	subarray = []
	k = 3
	while i <= len(array_1) - k - 1:
		print(i)
		subarray.append(array_1[i])

		if j < k - 1:
			j += 1
			i += 1
			continue

		print(subarray)
		subarray.pop(0)
		i += 1








array_1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# print_subarrays2(array_1)
print("-----------------")
step1(array_1)
step2(array_1)
step3(array_1)
step4(array_1)
step5(array_1)
step6(array_1)
