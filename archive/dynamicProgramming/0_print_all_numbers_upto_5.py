



def print_numbers1(total):
    print(total)
    total += 1
    print_numbers2(total)
def print_numbers2(total):
    print(total)
    total += 1
    print_numbers3(total)

def print_numbers3(total):
    if total == 2:
        print("Stop")
        return

print_numbers1(0)
