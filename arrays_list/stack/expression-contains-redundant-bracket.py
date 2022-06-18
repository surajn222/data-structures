
def check_redundant_brackets(str_parenthesis):
    print(f"\n\n\n")
    print(str_parenthesis)
    stack = []
    count_of_balanced_parenthesis = 0
    list_tuple =[]

    for character_in_strparenthesis in str_parenthesis:


        if character_in_strparenthesis in [")"]:
            if len(stack) == 0:
                print("Not okay, stack empty")
                continue

            character_in_stack = stack[-1]
            stack.pop()


            print("char in P: " + character_in_strparenthesis)
            print("char in stack: " + character_in_stack)
            flag_redundant_brackets = True
            if character_in_strparenthesis == ")":
                while(character_in_stack not in  ["("]):
                    character_in_stack = stack[-1]
                    stack.pop()

                    if character_in_stack == "+":
                        flag_redundant_brackets = False
            if flag_redundant_brackets == True:
                print(flag_redundant_brackets)
                return

        else:
            stack.append(character_in_strparenthesis)

    if stack:
        print("Not Okay, stack is not empty")


    print(flag_redundant_brackets)






if __name__ == "__main__":

    str_parenthesis_1 = "(a+b)"
    str_parenthesis_2 = "((a+b))"
    str_parenthesis_3 = "((a+b))"
    str_parenthesis_4 = "((a)+(b)+(a+b))"
    check_redundant_brackets(str_parenthesis_1)
    check_redundant_brackets(str_parenthesis_2)
    check_redundant_brackets(str_parenthesis_3)
    check_redundant_brackets(str_parenthesis_4)
