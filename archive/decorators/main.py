def outer_function(inner_function_passed_as_parameter):
    def return_function(*args, **kwargs):
        print("before inner function Execution")
        # getting the returned value
        returned_value = inner_function_passed_as_parameter(*args, **kwargs)
        print("after inner function Execution")
        # returning the value to the original frame
        return returned_value

    return return_function


# adding decorator to the function
@outer_function
def inner_function(a, b):
    print("inner function execution")
    return a + b

a, b = 1, 2

# getting the value through return of the function
print("Sum =", inner_function(a, b))