
def check_balanced_parenthesis(str_parenthesis):
    print(f"\n\n\n")
    print(str_parenthesis)

    stack = []
    count_of_balanced_parenthesis = 0
    list_tuple =[]
    index = 0

    for character_in_strparenthesis in str_parenthesis:


        if character_in_strparenthesis in [")", "]", "}"]:
            if len(stack) == 0:
                print("Not okay, stack empty")
                continue

            character_in_stack = stack[-1]
            stack.pop()


            print("char in P: " + character_in_strparenthesis)
            print("char in stack: " + character_in_stack)
            reverse_index = index
            if character_in_strparenthesis == ")":
                while(character_in_stack not in  ["("]):
                    character_in_stack = stack[-1]
                    stack.pop()
                    reverse_index-=1
                    print("Reverse index:" + str(reverse_index))
            elif character_in_strparenthesis == "]":
                while(character_in_stack not in  ["["]):
                    character_in_stack = stack[-1]
                    stack.pop()
                    reverse_index-=1
                    print("Reverse index:" + str(reverse_index))
            elif character_in_strparenthesis == "}":
                while(character_in_stack not in  ["{"]):
                    character_in_stack = stack[-1]
                    stack.pop()
                    reverse_index-=1
                    print("Reverse index:" + str(reverse_index))

            tuple = (reverse_index , index)

            list_tuple.append(tuple)
        else:
            stack.append(character_in_strparenthesis)
        index += 1

    print(list_tuple)
    if stack:
        print("Not Okay, stack is not empty")





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
