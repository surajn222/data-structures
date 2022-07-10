
def check_balanced_parenthesis(str_parenthesis):
    print(str_parenthesis)

	stack_temp = []
	count_of_balanced_parenthesis = 0

	for char_in_strparenthesis in str_parenthesis:
		if char_in_strparenthesis in ["(", "[", "{"]:
			stack_temp.append(char_in_strparenthesis)

		elif char_in_strparenthesis in [")", "]", "}"]:
			if len(stack_temp) == 0:
				print("Not okay, stack_temp empty")
				continue

			character_in_stack_temp = stack_temp.pop()

			if char_in_strparenthesis == ")" and character_in_stack_temp == "(":
				print("Okay")
				count_of_balanced_parenthesis += 1
			elif char_in_strparenthesis == "]" and character_in_stack_temp == "[":
				print("Okay")
				count_of_balanced_parenthesis += 1
			elif char_in_strparenthesis == "}" and character_in_stack_temp == "{":
				print("Okay")
				count_of_balanced_parenthesis += 1
			else:
				print("Not okay, brackets do not match")

	if stack_temp:
		print("Not Okay, stack_temp is not empty")

	print("Count of balanced parenthesis: " + str(count_of_balanced_parenthesis))

if __name__ == "__main__":

    str_parenthesis_1 = "(a+b)"
    str_parenthesis_2 = "[(a+b)]"
    str_parenthesis_3 = "(a+b))"
    str_parenthesis_4 = "[(a+b)"
    str_parenthesis_5 = "{a + (a+b)}"
    str_parenthesis_5 = "(a)([a+b])"
    check_balanced_parenthesis(str_parenthesis_1)
    check_balanced_parenthesis(str_parenthesis_2)
    check_balanced_parenthesis(str_parenthesis_3)
    check_balanced_parenthesis(str_parenthesis_4)
    check_balanced_parenthesis(str_parenthesis_5)
