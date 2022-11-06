def check_if_palindrome_recursion(i, str1):
	if i < len(str1) / 2:
		print("L = " + str(str1[i]) + " R = " + str1[len(str1) - 1 - i])
		if str1[i] == str1[len(str1) - 1 - i]:
			i = i + 1
			check_if_palindrome_recursion(i, str1)
		else:
			return False
	return True


str1 = "REFER"
print(check_if_palindrome_recursion(0, str1))
