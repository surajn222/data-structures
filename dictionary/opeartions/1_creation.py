#module_name, package_name, ClassName, method_name, ExceptionName, function_name, GLOBAL_CONSTANT_NAME, global_var_name, instance_var_name, function_parameter_name, local_var_name

#create an empty list
dict_dict_name = {}
dict_dict_name = dict()
print(dict_dict_name)

#create a list of nubers
dict_numbers = {"a": "1", "b": "2", "c": "3"}
print(dict_numbers)

#create a multi-dimensional list
dict_multi_dimensional = {"a": { "innera": 1}, "b": {"innerb": 2} }
print(dict_multi_dimensional)

#create a list of size
list_numbers = [1,2,3]
dict_of_size = [{i: i} for i in list_numbers]
print(dict_of_size)

#create a list of zeroes/ones/any character
list_zeroes = [0] * 10
dict_of_zeroes = [{i: i} for i in list_numbers] #This wont work, because the key is the same
print(list_zeroes)


