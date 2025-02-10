import os

print("HW")


def main():
	list_dirs = ["anagram", "binary", "combinations", "difference", "duplicate", "duplicates", "fix", "occurring",
				 "order", \
				 "palindrome", "pattern", "problem", "rearrange", "reverse", "rotate", "sub", "type"]

	for i in list_dirs:
		print(i)
		os.mkdir("../strings/strings_questions/" + str(i))


main()
