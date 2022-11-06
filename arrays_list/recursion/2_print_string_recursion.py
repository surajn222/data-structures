def print_string_recursion(str1):
	i = 0
	print("i = " + str(i))
	if i < len(str1):
		print(str1[0])
		i = i + 1
		print_string_recursion(str1[i:])


str1 = "STRING1"
print_string_recursion(str1)

# There are other better ways too
