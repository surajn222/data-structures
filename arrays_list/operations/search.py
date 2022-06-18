#create a list of nubers
list_numbers = [10, 20, 14]
print(list_numbers)

if 10 in list_numbers:
    print("10 Number present")

if 11 in list_numbers:
    print("11 Number present")
else:
    print("11 Number not present")

set_numbers = set(list_numbers)
print(set_numbers)
if 10 in set_numbers:
    print("10 Number present")

if 11 in set_numbers:
    print("11 Number present")
else:
    print("11 Number not present")
