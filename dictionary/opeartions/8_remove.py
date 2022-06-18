#create a dict of nubers
dict_numbers = {"a": "1", "b": "2", "c": "3"}
print(dict_numbers)

value = dict_numbers.pop('a', None)
print(value)
print(dict_numbers)

del dict_numbers['b']
print(dict_numbers)
