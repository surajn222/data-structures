def print_duplicates_recursion(str1):
	# print(len(str1))
	if str1 == "" or len(str1) < 2:
		return
	if str1[0] == str1[1]:
		print(str1[0])
	print_duplicates_recursion(str1[1:])


str1 = "AABAABCCDDD"
print_duplicates_recursion(str1)
